# Generated by Django 4.1.7 on 2023-03-12 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to=main.models.user_directory_path
                    ),
                ),
                (
                    "description",
                    models.CharField(blank=True, max_length=1500, null=True),
                ),
            ],
        ),
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
                ("image", models.ImageField(upload_to=main.models.user_directory_path)),
                ("is_primary", models.BooleanField(default=False)),
                ("slug", models.SlugField(default="image-slug", max_length=200)),
                ("name", models.CharField(default="imagename", max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="foodStand",
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
                ("name", models.CharField(max_length=100)),
                ("business_name", models.CharField(max_length=100)),
                (
                    "nv_business_id",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("phone_number", models.CharField(max_length=20)),
                ("description", models.TextField()),
                ("slug", models.SlugField(max_length=200)),
                ("status", models.BooleanField(default=True)),
                ("adress", models.CharField(blank=True, max_length=200, null=True)),
                ("city", models.CharField(blank=True, max_length=200, null=True)),
                ("state", models.CharField(blank=True, max_length=200, null=True)),
                ("zipcode", models.CharField(blank=True, max_length=200, null=True)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
                ("directions", models.CharField(blank=True, max_length=240, null=True)),
                ("website", models.URLField(blank=True, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("last_update", models.DateTimeField(auto_now=True)),
                (
                    "categories",
                    models.ManyToManyField(
                        related_name="foodstand", to="main.category"
                    ),
                ),
                (
                    "images",
                    models.ManyToManyField(related_name="foodstand", to="main.image"),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.AddIndex(
            model_name="foodstand",
            index=models.Index(fields=["id", "slug"], name="main_foodst_id_671b81_idx"),
        ),
        migrations.AddIndex(
            model_name="foodstand",
            index=models.Index(fields=["name"], name="main_foodst_name_1772fa_idx"),
        ),
        migrations.AddIndex(
            model_name="foodstand",
            index=models.Index(fields=["status"], name="main_foodst_status_309037_idx"),
        ),
    ]