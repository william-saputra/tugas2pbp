from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "price", "description", "thickness", "user_reviews", "user_ratings"]