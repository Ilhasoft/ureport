# Generated by Django 2.2.3 on 2019-08-20 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("orgs", "0026_fix_org_config_rapidpro"), ("stats", "0002_add_segments")]

    operations = [
        migrations.CreateModel(
            name="ContactActivity",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("contact", models.CharField(max_length=36)),
                ("born", models.IntegerField(null=True)),
                ("gender", models.CharField(max_length=1, null=True)),
                ("state", models.CharField(max_length=255, null=True)),
                ("district", models.CharField(max_length=255, null=True)),
                ("ward", models.CharField(max_length=255, null=True)),
                ("date", models.DateField(help_text="The starting date for for the month")),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="contact_activities", to="orgs.Org"
                    ),
                ),
            ],
            options={
                "unique_together": {("org", "contact", "date")},
                "index_together": {("org", "contact"), ("org", "date")},
            },
        )
    ]
