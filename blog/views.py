from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Post
from .forms import CommentForm

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def minha_view(request):
    context = {'mensagem': 'Olá, Mundo!'}
    return render(request, 'meu_template.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    # return render(request, 'blog/post_detail.html', {'post': post, 'form': form})
    return render(request, 'post_detail.html', {'post': post, 'form': form})