# Generated by Django 4.1.7 on 2023-03-09 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DataSchema",
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
                ("name", models.CharField(max_length=255)),
                (
                    "column_separator",
                    models.CharField(
                        choices=[(",", "Comma (,)"), (";", "Semicolon (;)")],
                        max_length=1,
                    ),
                ),
                (
                    "string_character",
                    models.CharField(
                        choices=[("“", "Double-quote (“)"), ("‘", "Apostrophes (‘)")],
                        max_length=1,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="GeneratedData",
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
                ("num_records", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[("PROCESSING", "Processing"), ("READY", "Ready")],
                        default="PROCESSING",
                        max_length=20,
                    ),
                ),
                ("file", models.FileField(null=True, upload_to="media/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "schema",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fake_csv.dataschema",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Column",
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
                ("name", models.CharField(max_length=255)),
                (
                    "data_type",
                    models.CharField(
                        choices=[
                            ("FULL_NAME", "Full name"),
                            ("JOB", "Job"),
                            ("EMAIL", "Email"),
                            ("DOMAIN_NAME", "Domain name"),
                            ("PHONE_NUMBER", "Phone number"),
                            ("COMPANY_NAME", "Company name"),
                            ("TEXT", "Text"),
                            ("INTEGER", "Integer"),
                            ("ADDRESS", "Address"),
                            ("DATE", "Date"),
                        ],
                        max_length=255,
                    ),
                ),
                ("range_from", models.IntegerField(blank=True, null=True)),
                ("range_to", models.IntegerField(blank=True, null=True)),
                ("order", models.IntegerField()),
                (
                    "schema",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="columns",
                        to="fake_csv.dataschema",
                    ),
                ),
            ],
        ),
    ]
