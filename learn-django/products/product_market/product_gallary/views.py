from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Product
from .serializers import ProductSerializer
import requests

# Create your views here.

products_url = "https://dummyjson.com/products?limit=200"


def get_product(request):
    products = requests.get(products_url).json()
    comments = {'comment': []}
    for prod in products["products"]:
        product_id = prod["id"]
        try:
            id_exist = Product.objects.get(id=product_id)
            continue
        except Product.DoesNotExist:
            product_ser = ProductSerializer(data=prod)
            product_ser.is_valid(raise_exception=True)
            product_ser.save()
        comment_data = requests.get(f"https://dummyjson.com/posts/{product_id}/comments").json()
        comments['comment'].append(comment_data['comments'])



    # obj = Product.objects.all()
    # serialized_prod = ProductSerializer(obj, many=True)
    # return JsonResponse({'status': 200, 'data': serialized_prod.data})

    return JsonResponse(comments)

