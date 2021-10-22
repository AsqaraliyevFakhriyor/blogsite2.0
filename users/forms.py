from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Custom Forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'age', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'age', 'email')
