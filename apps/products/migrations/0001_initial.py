# Generated by Django 5.0.1 on 2024-03-01 05:27

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("brands", "0001_initial"),
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(blank=True, max_length=256, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "mainimg",
                    models.ImageField(blank=True, null=True, upload_to="img/products/"),
                ),
                (
                    "price",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
                ),
                (
                    "stock_quantity",
                    models.PositiveIntegerField(blank=True, default=0, null=True),
                ),
                (
                    "brand",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="brands.brand"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="categories.category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
