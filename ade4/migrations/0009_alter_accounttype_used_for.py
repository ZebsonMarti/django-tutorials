# Generated by Django 3.2.13 on 2022-06-20 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ade4", "0008_auto_20220620_0947"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accounttype",
            name="used_for",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ORG", "Réunion Uniquement"),
                    ("MEMBER", "Membres Uniquement"),
                    ("BOTH", "Réunion et Membres"),
                ],
                default="BOTH",
                max_length=6,
                verbose_name="Pour",
            ),
        ),
    ]
