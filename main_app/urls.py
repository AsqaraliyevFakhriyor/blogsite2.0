from .views import home_page
from django.urls import path

# Create your urls here!
urlpatterns = [
    path('', home_page, name = "homepage")
]