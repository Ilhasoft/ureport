# Generated by Django 3.2.6 on 2021-10-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bots", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bot",
            name="deeplink",
            field=models.URLField(blank=True, help_text="The deeplink for this bot, optional", null=True),
        ),
        migrations.AlterField(
            model_name="bot",
            name="description",
            field=models.TextField(blank=True, help_text="The description of this bot, optional", null=True),
        ),
    ]
