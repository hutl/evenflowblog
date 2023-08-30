from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Post, Comentario
from .forms import AddComentario


def index(request):
    postagens = Post.objects.all()
    context = {
        'post_template': postagens
    }
    return render(request, 'index.html',context)

def detail(request,postId):
    post = Post.objects.get(id=postId)
    comentario = Comentario.objects.filter(post_id = postId)
    if request.method == "POST":
        form = AddComentario(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post_id = post
            comentario.save()
            messages.success(request, 'Comentário adicionado')
            return redirect('blog:index')
    form = AddComentario()
    context = {
        'postagem':post,
        'comentários': comentario,
        "formulário":form
    }
    return render(request,'detail.html',context)