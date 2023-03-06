# import qrcode
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import CategoryForm, ImageForm, LocationUpdateForm, foodStandForm
from .models import Category, Image, foodStand


def home(
    request,
):
    foodstands = foodStand.objects.all()

    context = {
        "foodstands": [],
        "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
    }
    for foodstand in foodstands:
        primary_image = foodstand.images.filter(is_primary=True).first()
        context["foodstands"].append((foodstand, primary_image))
    return render(request, "main/home.html", context)


def about(request):
    context = {"breadcrumb": [("Home", "/"), ("About", request.path)]}
    return render(request, "main/about.html", context)


def contact(request):
    context = {"breadcrumb": [("Home", "/"), ("Contact", request.path)]}
    return render(request, "main/contact.html", context)


def food_stand_detail(request, pk, slug):
    foodstand = get_object_or_404(foodStand, pk=pk, slug=slug)
    primary_image = foodstand.images.filter(is_primary=True).first()

    context = {
        "foodstand": foodstand,
        "primary_image": primary_image,
        "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
        "breadcrumb": [
            ("Home", "/"),
            ("Food Stand List", "/food_stand/"),
            (foodstand.name, request.path),
        ],
    }
    return render(request, "main/food_stand_detail.html", context)


@login_required
def food_stand_create(request):
    if request.method == "POST":
        form = foodStandForm(request.POST, request.FILES)
        if form.is_valid():
            foodstand = form.save(commit=False)
            foodstand.owner = request.user
            foodstand.save()
            form.save_m2m()
            for image in request.FILES.getlist("images"):
                img = Image.objects.create(image=image)
                foodstand.images.add(img)
            messages.success(request, "Food Stand created successfully.")
            return redirect("main:food_stand_detail", pk=foodstand.pk)
    else:
        form = foodStandForm()
    return render(request, "main/food_stand_create.html", {"form": form})


@login_required
def category_create(request):
    if request.method == "POST":
        category = CategoryForm(request.POST, request.FILES)
        if category.is_valid():
            category = category.save()
            messages.success(request, "Category created successfully.")
            next_url = request.GET.get("next", reverse("main:home"))
            return redirect(next_url, slug=category.slug)
    else:
        category = CategoryForm()
    return render(request, "main/category_create.html", {"category": category})


@login_required
def food_stand_update(request, pk):
    foodstand = get_object_or_404(foodStand, pk=pk)
    if foodstand.owner != request.user:
        return redirect("main:food_stand_detail", pk=pk)
    if request.method == "POST":
        form = foodStandForm(request.POST, instance=foodstand)
        if form.is_valid():
            foodstand = form.save()
            for image in request.FILES.getlist("images"):
                img = Image.objects.create(image=image)
                foodstand.images.add(img)
            messages.success(request, "Food Stand updated successfully.")
            return redirect("main:food_stand_detail", pk=foodstand.pk)
    else:
        form = foodStandForm(instance=foodstand)
    return render(
        request, "main/food_stand_update.html", {"form": form, "foodstand": foodstand}
    )


@login_required
def food_stand_images(request, pk):
    foodstand = get_object_or_404(foodStand, pk=pk)
    images = foodstand.images.all()
    if foodstand.owner != request.user:
        return redirect("main:food_stand_detail", pk=pk)
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if "set_primary" in request.POST:
            primary_image_id = request.POST.get("id")
            for image in images:
                if str(image.id) == primary_image_id:
                    image.is_primary = True
                else:
                    image.is_primary = False
                image.save()
            messages.success(request, "Primary image set successfully.")
        elif "delete_image" in request.POST:
            image_id = request.POST.get("id")
            image = get_object_or_404(Image, id=image_id)
            image.delete()
            messages.success(request, "Image deleted successfully.")
        else:
            if form.is_valid():
                for image in request.FILES.getlist("images"):
                    img = Image.objects.create(image=image)
                    foodstand.images.add(img)

                messages.success(request, "Images uploaded successfully.")
            return redirect("main:food_stand_images", pk=pk)
    else:
        form = ImageForm()
    context = {
        "foodstand": foodstand,
        "images": images,
        "form": form,
    }
    return render(request, "main/food_stand_images.html", context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    foodstands = foodStand.objects.filter(categories=category)
    context = {
        "category": category,
        "foodstands": foodstands,
        "breadcrumb": [("Home", "/"), ("Category List", request.path)],
    }
    return render(request, "main/category_detail.html", context)


def food_stand_list(request):
    categories = Category.objects.all()
    selected_category = request.GET.get("category")
    if selected_category:
        foodstands = foodStand.objects.filter(categories__slug=selected_category)
        category = get_object_or_404(Category, slug=selected_category)
    else:
        foodstands = foodStand.objects.all()
        category = None

    breadcheck = []
    if not category:
        breadcheck = "All"
    else:
        breadcheck = category

    context = {
        "categories": categories,
        "foodstands": [],
        "category": category,
        "breadcrumb": [("Home", "/"), (breadcheck, request.path)],
    }

    for foodstand in foodstands:
        primary_image = foodstand.images.filter(is_primary=True).first()
        context["foodstands"].append((foodstand, primary_image))

    return render(request, "main/food_stand_list.html", context)


@login_required
def update_location(request, id):
    food_stand = foodStand.objects.get(id=id)
    if request.method == "POST":
        form = LocationUpdateForm(request.POST, instance=food_stand)
        if form.is_valid():
            form.save()
            return redirect("main:food_stand_detail", pk=id)
    else:
        initial_data = {}
        latitude = request.GET.get("latitude")
        longitude = request.GET.get("longitude")
        if latitude and longitude:
            initial_data["latitude"] = latitude
            initial_data["longitude"] = longitude
        form = LocationUpdateForm(instance=food_stand, initial=initial_data)

    context = {
        "form": form,
    }
    return render(request, "main/update_location.html", context)


# def location_qr_code_view(request, id):
#     # Get the foodStand object based on the ID
#     food_stand = foodStand.objects.get(id=id)

#     # Construct the URL for the update_location view
#     url = reverse('main:update_location', args=[id])

#     # Generate the QR code image
#     qr = qrcode.QRCode(version=1, box_size=10, border=4)
#     qr.add_data(request.build_absolute_uri(url))
#     qr.make(fit=True)
#     img = qr.make_image(fill_color="black", back_color="white")

#     # Return the QR code image as an HTTP response
#     response = HttpResponse(content_type="image/png")
#     img.save(response, "PNG")
#     return response
