from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(request, 'blog/blog.html')

def detail_blog(request):
    return render(request, 'blog/single-blog.html')