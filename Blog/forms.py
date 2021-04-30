from django import forms
from .models import Post
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content']
        labels = {
            "title": "Başlık",
            "subtitle": "Alt Başlık",
            "content": "İçerik"
        }