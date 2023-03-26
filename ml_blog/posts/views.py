from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Post, Author, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *

def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gallery')

    return render(request, 'photos/login_register.html', {'page': page})


def viewPost(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'posts/post.html', {'post': post})


def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post.html', {'post': post})


@login_required(login_url='login')
def posts(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        posts = Post.objects.filter(category__user=user)
    else:
        posts = Post.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'posts': posts}
    return render(request, 'posts/posts.html', context)
