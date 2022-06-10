# Generated by Django 4.0.5 on 2022-06-10 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ade4", "0003_constants"),
    ]

    operations = [
        migrations.CreateModel(
            name="Meeting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("date", models.DateField(verbose_name="Date")),
                (
                    "address",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="ade4.address",
                    ),
                ),
            ],
            options={
                "verbose_name": "Meeting",
                "ordering": ["-date"],
            },
        ),
    ]
