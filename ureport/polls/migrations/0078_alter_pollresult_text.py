# Generated by Django 5.0.8 on 2024-09-18 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0077_rename_poll_org_published_id_polls_poll_org_pblshd_id_idx_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pollresult",
            name="text",
            field=models.TextField(max_length=1600, null=True),
        ),
    ]
