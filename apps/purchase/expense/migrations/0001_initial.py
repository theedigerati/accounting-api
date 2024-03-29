# Generated by Django 5.0.3 on 2024-03-21 16:29

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounting", "0002_journalentry_journalentryline"),
        ("tax", "0001_initial"),
        ("vendor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Expense",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=12)),
                ("tax_inclusive", models.BooleanField(default=False)),
                ("date", models.DateField(default=datetime.date.today)),
                ("notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounting.account",
                    ),
                ),
                (
                    "paid_through",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="expenses_paid_through",
                        to="accounting.account",
                    ),
                ),
                ("taxes", models.ManyToManyField(blank=True, to="tax.tax")),
                (
                    "vendor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="vendor.vendor",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
