# Generated by Django 5.1 on 2024-09-05 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("diary", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("created_dt", models.DateTimeField(auto_now_add=True)),
                ("updated_dt", models.DateTimeField(auto_now=True)),
                ("prompt", models.TextField(blank=True)),
                ("url", models.CharField(max_length=1024)),
                (
                    "diary",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="diary.diary"
                    ),
                ),
            ],
            options={
                "db_table": "image",
            },
        ),
    ]
