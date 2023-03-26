from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),

    # path('login/', views.loginUser, name="login"),
    # path('logout/', views.logoutUser, name="logout"),
    # path('register/', views.registerUser, name="register"),

    path('post/<str:pk>/', views.viewPost, name='post'),
    # path('add/', views.addPhoto, name='add'),
]