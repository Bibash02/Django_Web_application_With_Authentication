from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post

# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Password do not match.")
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')
        
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Registration successful.")
        return redirect('login')
    return render(request, 'register.html')

def signin(request):
    if request.method  == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username = user_obj.username, password = password)
        except User.DoesNotExist:
            user = None
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')
        
    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('login')

def home(request):
    blogs = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'blogs': blogs})

def profile(request):
    return render(request, 'profile.html')

def blog(request):
    blogs = Post.objects.filter(author=request.user)
    return render(request, 'blog.html', {'blogs': blogs})

def create_blog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title = title, content = content, author = request.user)
        return redirect('blog')
    return render(request, 'blog_create.html')

def blog_detail(request, post_id):
    pass

def delete_blog(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    post.delete()
    return redirect('blog')

def password_reset_email(request):
    return render(request, 'password_reset_email.html')

def password_reset_form(request, token):
    return render(request, 'password_reset_form.html', {'token': token})