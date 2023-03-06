from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    # path('food_stands/', views.foodStands, name='food_stands'),
    # path('food_stands/<slug:category_slug>/', views.foodStands, name='food_stand_list_by_category'),
    # path('food_stand_detail/<int:id>/<slug:slug>/', views.foodStand_detail, name='food_stand_detail'),
    path("food_stand/", views.food_stand_list, name="food_stand_list"),
    path(
        "food_stand/<int:pk>/<slug:slug>/",
        views.food_stand_detail,
        name="food_stand_detail",
    ),
    path("food_stand/create/", views.food_stand_create, name="food_stand_create"),
    path(
        "food_stand/<int:pk>/<slug:slug>/update/",
        views.food_stand_update,
        name="food_stand_update",
    ),
    path(
        "food_stand/<int:pk>/<slug:slug>/update-location/",
        views.update_location,
        name="update_location",
    ),
    # path('food_stand/<int:pk>/images/', views.food_stand_images, name='food_stand_images'),
    # path('food_stand/delete/<int:pk>/images/', views.delete_image, name='delete_image'),
    path("category/create/", views.category_create, name="category_create"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),
    path(
        "food_stand/<int:pk>/<slug:slug>/images/",
        views.food_stand_images,
        name="food_stand_images",
    ),
    # path('food_stand/<int:pk>/images/<int:image_pk>/set_first/', views.set_first_image, name='set_first_image'),
    # path('categories/<int:pk>/', views.category_detail, name='category_detail'),
]
