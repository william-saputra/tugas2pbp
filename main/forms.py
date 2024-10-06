from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags
from django import forms  # Ensure forms is imported

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "price", "description", "thickness", "user_reviews", "user_ratings"]

    def clean_product_name(self):
        product_name = self.cleaned_data["product_name"]
        return strip_tags(product_name)  # Clean product name by stripping HTML tags

    # Clean description
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)  # Clean description by stripping HTML tags

    # Clean user_reviews
    def clean_user_reviews(self):
        user_reviews = self.cleaned_data["user_reviews"]
        return strip_tags(user_reviews)  # Clean user reviews by stripping HTML tags