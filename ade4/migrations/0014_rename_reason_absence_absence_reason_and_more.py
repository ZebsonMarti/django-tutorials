# Generated by Django 4.0.5 on 2022-06-22 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ade4", "0013_aid_aid_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="absence",
            old_name="reason",
            new_name="absence_reason",
        ),
        migrations.RenameField(
            model_name="sanction",
            old_name="reason",
            new_name="sanction_reason",
        ),
    ]