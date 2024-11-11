from django.shortcuts import render

def index(request):
    return render(request, 'microblog/index.html')


def about(request):
    return render(request, 'microblog/about.html')