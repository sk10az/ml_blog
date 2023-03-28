from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<str:pk>/', views.viewPost, name='post'),
    # path('add/', views.addPhoto, name='add'),

    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('search/', views.search_results, name='search_results'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
]

