from django.urls import path
from .views import SignUpView

# write your urls here!
urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup')
]
