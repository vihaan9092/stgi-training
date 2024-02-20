import json
from django.shortcuts import render
from django.http import Http404

POSTS_FILE = 'blog/data/posts.json'

def load_posts():
    with open(POSTS_FILE, 'r') as file:
        posts = json.load(file)
    return posts

def landing_page(request):
    return render(request, 'blog/index.html')

def posts(request):
    posts = load_posts()
    return render(request, 'blog/all-posts.html', {'posts': posts})

def single_post(request, slug):
    posts = load_posts()
    post = next((post for post in posts if post['id'] == slug), None)
    if post is None:
        raise Http404('Post not found')
    return render(request, 'blog/single-post.html', {'post': post})
