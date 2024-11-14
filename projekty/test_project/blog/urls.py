from django.urls import path
from blog.views import index, about, cislo, username

urlpatterns = [
    path('', index), # /blog/
    path('about/', about), # /blog/about/
    # /blog/cislo/1000/
    # /blog/cislo/100/
    path('cislo/<int:number>/', cislo),
    path('username/<str:name>/', username),

    # /username/suche/
    # /username/jan/
    # /username/petr/
]