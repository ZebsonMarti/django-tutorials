# Generated by Django 4.0.5 on 2022-06-20 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ade4", "0012_alter_account_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="aid",
            name="aid_type",
            field=models.CharField(
                default="ASSISTANCE", max_length=10, verbose_name="Type Aide"
            ),
            preserve_default=False,
        ),
    ]
