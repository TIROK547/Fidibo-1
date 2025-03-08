from django.urls import path
from .views import product_hello_page,display_name
urlpatterns = [
    path("Hello/", product_hello_page),
    path("<str:name>", display_name),

]