from posts.models import Post

from django.shortcuts import render

# Create your views here.
#здесь настраивается отображение данных

def post_list(request):
    posts = Post.objects.all() #SELECT * FROM post_posts
    return render(request, context={'posts': posts})
