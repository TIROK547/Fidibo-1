from django.urls import path
from .views import product_hello_page,display_name,download_Dorcci
urlpatterns = [
    path("Hello/", product_hello_page),
    path("Dorrci/", download_Dorcci),
    path("<str:name>", display_name),


]