# Generated by Django 5.0.8 on 2024-08-23 13:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flows", "0002_alter_flowresult_unique_together_and_more"),
        ("orgs", "0033_rename_orgs_orgbac_org_id_607508_idx_orgs_orgbac_org_slug_idx_and_more"),
        ("polls", "0076_alter_poll_index_together"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="poll",
            new_name="polls_poll_org_pblshd_id_idx",
            old_fields=("org", "published", "id"),
        ),
        migrations.RenameIndex(
            model_name="pollquestion",
            new_name="polls_qstn_poll_actv_fl_rs_idx",
            old_fields=("poll", "is_active", "flow_result"),
        ),
        migrations.RenameIndex(
            model_name="pollresult",
            new_name="polls_rslt_org_flw_rst_txt_idx",
            old_fields=("org", "flow", "ruleset", "text"),
        ),
        migrations.RenameIndex(
            model_name="pollresult",
            new_name="polls_pollresult_org_flow_idx",
            old_fields=("org", "flow"),
        ),
        migrations.AlterUniqueTogether(
            name="pollcategory",
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name="pollquestion",
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name="pollresponsecategory",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="pollcategory",
            constraint=models.UniqueConstraint(
                fields=("name", "org"), name="polls_pollcategory_name_156693e034f96627_uniq"
            ),
        ),
        migrations.AddConstraint(
            model_name="pollquestion",
            constraint=models.UniqueConstraint(
                fields=("poll", "flow_result"), name="polls_pollquestion_poll_id_flow_result_id_608a2446_uniq"
            ),
        ),
        migrations.AddConstraint(
            model_name="pollquestion",
            constraint=models.UniqueConstraint(
                fields=("poll", "ruleset_uuid"), name="polls_pollquestion_poll_id_4202706c8106f06_uniq"
            ),
        ),
        migrations.AddConstraint(
            model_name="pollresponsecategory",
            constraint=models.UniqueConstraint(
                fields=("question", "rule_uuid"), name="polls_pollresponsecategory_question_id_3a161715511bd77d_uniq"
            ),
        ),
        migrations.AddConstraint(
            model_name="pollresponsecategory",
            constraint=models.UniqueConstraint(
                fields=("question", "flow_result_category"),
                name="polls_pollresponsecatego_question_id_flow_result__4db1cb7e_uniq",
            ),
        ),
    ]