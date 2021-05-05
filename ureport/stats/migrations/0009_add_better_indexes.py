# Generated by Django 2.2.20 on 2021-04-27 14:50

from django.db import migrations

# language=SQL
INDEX_SQL_CONTACTACTIVITY_ORG_DATE_GENDER_NOT_NULL = """
CREATE INDEX IF NOT EXISTS stats_contactactivity_org_id_date_gender_not_null on stats_contactactivity (org_id, date, gender) WHERE gender IS NOT NULL;
"""

# language=SQL
INDEX_SQL_CONTACTACTIVITY_ORG_DATE_STATE_NOT_NULL = """
CREATE INDEX IF NOT EXISTS stats_contactactivity_org_id_date_state_not_null on stats_contactactivity (org_id, date, state) WHERE state IS NOT NULL;
"""


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0008_add_index"),
    ]

    operations = [
        migrations.RunSQL(INDEX_SQL_CONTACTACTIVITY_ORG_DATE_GENDER_NOT_NULL),
        migrations.RunSQL(INDEX_SQL_CONTACTACTIVITY_ORG_DATE_STATE_NOT_NULL),
    ]
