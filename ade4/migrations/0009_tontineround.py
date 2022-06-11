# Generated by Django 4.0.5 on 2022-06-10 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ade4", "0008_alter_hosts_options_alter_hosts_unique_together"),
    ]

    operations = [
        migrations.CreateModel(
            name="TontineRound",
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
                ("pots", models.FloatField(default=1, verbose_name="NB Noms")),
                (
                    "amount_per_pot",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "end_date",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="end_tontine_round",
                        to="ade4.meeting",
                    ),
                ),
                (
                    "start_date",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="start_tontine_round",
                        to="ade4.meeting",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tontine Round",
                "verbose_name_plural": "Tontine Rounds",
                "ordering": ["-start_date__date"],
            },
        ),
    ]
