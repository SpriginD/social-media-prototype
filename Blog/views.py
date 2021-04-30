from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, CreatePostForm
from .models import Post
import datetime

def index(request):
    return render(request, 'index.html', {})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {})

def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'posts.html', {'all_posts':all_posts})

def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = datetime.datetime.now()
            post.save()
            return redirect('posts')
    else:
        form = CreatePostForm()
    return render(request, 'create.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, Hesabınız başarıyla oluşturulmuştur. Artık giriş yapabilirsiniz.')
            return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})

def login(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('/')