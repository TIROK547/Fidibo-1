from django.urls import path
from .views import product_hello_page,display_name,download_Dorcci,your_info
urlpatterns = [
    path("Hello/", product_hello_page),
    path("Dorrci/", download_Dorcci),
    path("Hello/info/", your_info),
    path("<str:name>", display_name),


]