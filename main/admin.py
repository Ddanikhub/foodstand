from django.contrib import admin

from .models import Category, Image, foodStand

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(foodStand)
class foodStandAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "owner", "status", "latitude", "longitude"]
    list_filter = [
        "name",
        "status",
    ]
    list_editable = ["status", "latitude", "longitude"]
    prepopulated_fields = {"slug": ("name",)}

    def image_preview(self, obj):
        images = obj.image.all()[:3]
        return ", ".join([str(image.image) for image in images])

    image_preview.short_description = "Images"


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "foodstand", "image", "is_primary")
    list_display_links = ("id", "image")
