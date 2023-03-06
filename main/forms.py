from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Field, Layout, Submit
from django import forms

from .models import Category, Image, foodStand


class foodStandForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    new_category_name = forms.CharField(label="New Category Name", required=False)
    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}), required=False
    )

    class Meta:
        model = foodStand
        fields = [
            "name",
            "phone_number",
            "description",
            "adress",
            "city",
            "state",
            "zipcode",
            "latitude",
            "longitude",
            "website",
            "categories",
            "nv_business_id",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Create"))
        self.helper.layout = Layout(
            Field("categories"),
            HTML(
                '<a href="{% url "main:category_create" %}?next={{ request.path }}" class="button-link ">'
                '<button type="button" class="btn btn-primary mb-3">Category Create</button></a>'
            ),
            FloatingField("name"),
            FloatingField("phone_number"),
            FloatingField("nv_business_id", required=True),
            FloatingField("description"),
            FloatingField("adress"),
            FloatingField("city"),
            FloatingField("state"),
            FloatingField("zipcode"),
            FloatingField("latitude"),
            FloatingField("longitude"),
            FloatingField("website"),
            FloatingField("images"),
        )
        self.fields["nv_business_id"].label = "NV Business ID"
        self.fields["categories"].widget.attrs.update(
            {"class": "form-select", "size": 10}
        )


class ImageForm(forms.ModelForm):
    images = forms.ImageField(
        required=False, widget=forms.ClearableFileInput(attrs={"multiple": True})
    )
    set_primary = forms.BooleanField(required=False, label="Set as primary")

    class Meta:
        model = Image
        fields = ["images", "set_primary"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Upload"))
        self.helper.form_tag = False
        self.helper.layout = Layout(
            FloatingField("images"),
        )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "image", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Create"))


class LocationUpdateForm(forms.ModelForm):
    class Meta:
        model = foodStand
        fields = ["latitude", "longitude"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Update"))
        self.helper.layout = Layout("latitude", "longitude")
