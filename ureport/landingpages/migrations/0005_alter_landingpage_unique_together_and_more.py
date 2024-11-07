# Generated by Django 5.0.8 on 2024-08-23 13:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bots", "0006_alter_bot_created_by_alter_bot_modified_by"),
        ("landingpages", "0004_alter_landingpage_created_by_and_more"),
        ("orgs", "0033_rename_orgs_orgbac_org_id_607508_idx_orgs_orgbac_org_slug_idx_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="landingpage",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="landingpage",
            constraint=models.UniqueConstraint(
                fields=("org", "slug"), name="landingpages_landingpage_org_id_slug_f7f1304e_uniq"
            ),
        ),
    ]
