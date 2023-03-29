from django.shortcuts import render

# Create your views here.
lista= {
    'productos':{
    },
    'categorias':{

    }
}


def productos(request):
    context={lista}
    return render(request, 'productos.html',context)


def categorias(request):
    context={lista}
    return render(request,'categorias.html',context)