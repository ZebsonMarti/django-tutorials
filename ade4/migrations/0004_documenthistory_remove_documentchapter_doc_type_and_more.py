# Generated by Django 4.0.5 on 2022-06-16 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ade4", "0003_alter_board_end_date_alter_board_start_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="DocumentHistory",
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
                ("content", models.TextField()),
                ("comment", models.TextField()),
                (
                    "document_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="document",
                        to="ade4.documenttype",
                    ),
                ),
            ],
            options={
                "verbose_name": "Document",
                "verbose_name_plural": "Documents",
                "ordering": ["-updated_at"],
            },
        ),
        migrations.RemoveField(
            model_name="documentchapter",
            name="doc_type",
        ),
        migrations.DeleteModel(
            name="DocumentArticle",
        ),
        migrations.DeleteModel(
            name="DocumentChapter",
        ),
    ]