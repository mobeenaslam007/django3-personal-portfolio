from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def all_blogs(request):
    blogs = Blog.objects.order_by("-date") # Sort in descending order on the basis of date
    return render(request, "blogs/all_blogs.html", {"blogs": blogs})

def details(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blogs/details.html", {"details": details})
