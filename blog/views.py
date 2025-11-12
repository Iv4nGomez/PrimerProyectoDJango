from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Autor
from .forms import AutorForm

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

def formulario(request):
    if request.method == 'GET':
        print(f"METODO: {request.method}")
        return render(request, 'blog/form.html')
    
def autor_nuevo(request):
    if request.method == 'POST':
        print(request.POST)
        form = AutorForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data('nombre')
            apellidos = form.cleaned_data('apellidos')
            fecha_nac = form.cleaned_data('fecha_nac')

            Autor.objects.create(nombre=nombre, apellidos=apellidos, fecha_nac=fecha_nac)
            return redirect('autores')
    else:
        form = AutorForm()

    return render(request, 'blog/autor_nuevo.html', {'form': form})

