from django.http.response import HttpResponse
import os


def product_hello_page(request):
    return HttpResponse("Hello this is hello page")


def display_name(request, name):
    return HttpResponse(f"Hello {name} welcome!")



