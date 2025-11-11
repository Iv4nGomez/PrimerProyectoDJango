from django.shortcuts import render, get_object_or_404
from .models import Post, Autor

# Create your views here.

def inicio (request):
    contexto = {"entradas": Post.objects.all(), "autores": Autor.objects.all()}
    return render(request, 'blog/inicio.html', contexto)

def detalles_post(request, pk):
    contexto = {"entradas": get_object_or_404(Post, pk=pk)}
    # contexto = get_object_or_404({"entradas": Post.objects.get(id=pk)})  
    return render(request, f'blog/detalles_post.html', contexto)

def autor_post(request, pk):
    contexto = {"entradas": Post.objects.filter(autor=pk)}
    autor = get_object_or_404(Autor, pk=pk)
    contexto["autor"] = autor
    print(contexto)
    return render(request,f"blog/autores_post.html", contexto)

def autores(request):
    contexto = {"autores": Autor.objects.all()}
    return render(request, "blog/autores.html" , contexto)