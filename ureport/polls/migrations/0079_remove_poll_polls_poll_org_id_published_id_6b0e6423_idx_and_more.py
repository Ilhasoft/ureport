# Generated by Django 5.1.2 on 2024-10-22 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0078_alter_pollresult_text"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="poll",
            name="polls_poll_org_id_published_id_6b0e6423_idx",
        ),
        migrations.RemoveIndex(
            model_name="pollquestion",
            name="polls_pollquestion_poll_id_is_active_flow_r_deda78e0_idx",
        ),
        migrations.RemoveIndex(
            model_name="pollresult",
            name="polls_pollresult_org_id_dfd50a4d782b673_idx",
        ),
        migrations.RemoveIndex(
            model_name="pollresult",
            name="polls_pollresult_org_id_68705a7f5a6456ed_idx",
        ),
    ]