# Generated by Django 2.2.20 on 2021-07-27 15:41

import time

from django.db import migrations
from django.db.models import Count

from ureport.utils import chunk_list


def noop(apps, schema_editor):  # pragma: no cover
    pass


def score(obj):
    obj_score = 0

    # hidden categories
    if not obj.is_active:
        return 0

    # when we have a mix for is_active False and True, True is the best to keep
    if obj.is_active:
        obj_score += 1

    # category dispaly was set
    if obj.category_displayed is not None:
        obj_score += 2

        # category display has been updated that should be the best to keep
        if obj.category_displayed != obj.category:
            obj_score += 4

    return obj_score


def deduplicate_pollresponsecategories(apps, schema_editor):  # pragma: no cover
    PollResponseCategory = apps.get_model("polls", "PollResponseCategory")

    PollStats = apps.get_model("stats", "PollStats")

    start_time = time.time()
    count = 0

    duplicates = (
        PollResponseCategory.objects.all()
        .values("question", "flow_result_category")
        .annotate(Count("id"))
        .annotate(Count("is_active", distinct=True))
        .filter(id__count__gte=2)
    )

    for duplicate in duplicates:

        duplicate_objs = PollResponseCategory.objects.filter(
            question_id=duplicate["question"],
            flow_result_category_id=duplicate["flow_result_category"],
        )
        choosen_one = duplicate_objs.first()
        choosen_score = score(choosen_one)

        # select the best to keep
        for obj in duplicate_objs:
            obj_score = score(obj)

            if obj_score > choosen_score:
                choosen_one = obj
                choosen_score = obj_score

        # poll response categories ids to remove
        poll_response_categories_ids = list(
            PollResponseCategory.objects.filter(
                question_id=duplicate["question"],
                flow_result_category_id=duplicate["flow_result_category"],
            )
            .exclude(id=choosen_one.pk)
            .values_list("id", flat=True)
        )

        # update foreign key for their stats
        category_stats_ids = PollStats.objects.filter(category_id__in=poll_response_categories_ids).values_list(
            "id", flat=True
        )
        for batch in chunk_list(category_stats_ids, 1000):
            stats_batch = list(batch)
            updated = PollStats.objects.filter(id__in=stats_batch).update(category_id=choosen_one.id)
            count += updated
            elapsed = time.time() - start_time
            print(f"Migrated {count} poll stats for duplicated categories in {elapsed:.1f} seconds")

        assert not PollStats.objects.filter(category_id__in=poll_response_categories_ids).exists()

        # safe to remove them now
        PollResponseCategory.objects.filter(id__in=poll_response_categories_ids).delete()

    assert (
        not PollResponseCategory.objects.all()
        .values("question", "flow_result_category")
        .annotate(Count("id"))
        .filter(id__count__gte=2)
        .exists()
    )
    print("Finished deduplicating the poll response categories")


def apply_manual():  # pragma: no cover
    from django.apps import apps

    deduplicate_pollresponsecategories(apps, None)


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0063_auto_20210716_1503"),
    ]

    operations = [migrations.RunPython(deduplicate_pollresponsecategories, noop)]
