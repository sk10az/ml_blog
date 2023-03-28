from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Post, Author, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import *


def viewPost(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'posts/post.html', {'post': post})


@login_required(login_url='login')
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



def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('posts')

    return render(request, 'posts/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('posts')

    context = {'form': form, 'page': page}
    return render(request, 'posts/login_register.html', context)


def search_results(request):
    query = request.GET.get('query')
    results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    context = {'results': results}
    return render(request, 'posts/search_results.html', context)


def post_list(request):
    query = request.GET.get('query')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    query = request.GET.get('query')
    if query:
        related_posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).exclude(pk=pk)
    else:
        related_posts = Post.objects.filter(category=post.category).exclude(pk=pk)
    context = {'post': post, 'related_posts': related_posts}
    return render(request, 'posts/post_detail.html', context)
