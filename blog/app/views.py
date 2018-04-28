from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
def post_list (request):
    print(request)
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by("-created_date")
    return render (request, 'app/post_list.html', {"posts":posts})
def post_detail (request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'app/post_detail.html', {"post": post})
# Create your views here.
