from django.shortcuts import render
from blog.models import Blogpost

# Create your views here.
def index(request):
    blogPost = Blogpost.objects.all()
    return render(request, 'blog/index.html', {'blogPost' : blogPost})

def blogPost(request, id):
    blogPost = Blogpost.objects.get(post_id=id)
    next_id = blogPost.post_id + 1
    prev_id = blogPost.post_id - 1
    if(prev_id == 0):
        prev_id = 1

    return render(request, 'blog/blogpost.html', {'blogs':blogPost, 'prev_id':prev_id, 'next_id':next_id})