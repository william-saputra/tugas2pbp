from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.utils.html import strip_tags

import json

from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    # product_entries = Product.objects.filter(user=request.user) --> udah tidak digunakan krn sekarang pakai json
    context = {
        'name': request.user.username,
        'app' : 'Box Synthetic Leather',
        'name': 'William Matthew Saputra',
        'class': 'PBP F',   
        'npm': '2306165862',
        # 'product_entries' : product_entries,--> udah tidak digunakan krn sekarang pakai json
        'last_login': request.COOKIES.get('last_login', 'Not Available'),
   
    }

    return render(request, "main.html", context)

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    product_name = strip_tags(request.POST.get("product_name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    thickness = request.POST.get("thickness")
    user_reviews = strip_tags(request.POST.get("user_reviews"))
    user_ratings = request.POST.get("user_ratings")
    user = request.user

    new_product = Product(
        product_name=product_name, price=price,
        description=description, thickness=thickness,
        user_reviews=user_reviews, user_ratings=user_ratings,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)


def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        # form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
        messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get product entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get product berdasarkan id
    product = Product.objects.get(pk = id)
    # Hapus product
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

            # Buat entri baru berdasarkan data yang dikirim
        new_product = Product.objects.create(
            user=request.user,
            product_name=data.get("product_name"),
            price=float(data.get("price")),
            description=data.get("description"),
            thickness=float(data.get("thickness")),
            user_reviews=data.get("user_reviews"),
            user_ratings=float(data.get("user_ratings")),
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)