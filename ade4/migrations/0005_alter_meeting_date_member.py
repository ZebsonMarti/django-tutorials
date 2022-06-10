# Generated by Django 4.0.5 on 2022-06-10 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ade4", "0004_meeting"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meeting",
            name="date",
            field=models.DateField(unique=True, verbose_name="Date"),
        ),
        migrations.CreateModel(
            name="Member",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("name", models.CharField(max_length=100, verbose_name="Full Name")),
                (
                    "address",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ade4.address",
                        to_field="raw_address",
                    ),
                ),
                (
                    "register_date",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ade4.meeting",
                        to_field="date",
                    ),
                ),
                ("skills", models.ManyToManyField(to="ade4.skill")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
