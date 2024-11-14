from django.shortcuts import render, HttpResponse


def index(request):
    print(request.POST)
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def cislo(request, number):
    context = {'number': number}
    return render(request, 'blog/cislo.html', context)

def username(request, name):
    context = {'name': name} # pod názvem 'name' to bude k dispozici v template
    return render(request, 'blog/username.html', context)