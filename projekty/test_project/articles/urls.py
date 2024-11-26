from django.urls import path
from articles import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),
    path('clanek/<int:pk>/', views.article_detail, name='article_detail'),
    path('clanek/<int:pk>/comment/', views.create_comment, name='create_comment')
]