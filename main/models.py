from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from foodstand.users.models import User


def user_directory_path(instance, filename):
    return f"static/media/main/images/{instance._meta.verbose_name}/{filename}"


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    description = models.CharField(max_length=1500, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:food_stand_list_by_category", args=[self.slug])


class Image(models.Model):
    image = models.ImageField(upload_to=user_directory_path)
    is_primary = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, default="image-slug")
    name = models.CharField(max_length=200, default="imagename")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}"


class foodStand(models.Model):
    categories = models.ManyToManyField(Category, related_name="foodstand")
    images = models.ManyToManyField(Image, related_name="foodstand")
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    nv_business_id = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    description = models.TextField()
    slug = models.SlugField(max_length=200)
    status = models.BooleanField(default=True)
    adress = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    zipcode = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    directions = models.CharField(max_length=240, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["status"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:food_stand_detail", args=[self.id, self.slug])
