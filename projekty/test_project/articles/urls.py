from django.urls import path
from articles import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('clanek/<int:pk>/', views.article_detail, name='article_detail'),
]