from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, TemplateView, DeleteView, View
from .models import Producto, Carrito
from django.urls import reverse_lazy
from .forms import CarritoForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Sum


#nos lleva a inicio
class Consultar(ListView):
    model = Producto
    template_name = 'comercio/index.html'
    context_object_name = 'pro'
    queryset = Producto.objects.all()

#nos lleva a ella
class ConsultarElla(ListView):
    model = Producto
    template_name = 'comercio/paraElla.html'
    context_object_name = 'pro'
    queryset = Producto.objects.filter(tipo='F')


def busqueda(self):
    q = request.GET.get('q', '')
    eventos = Producto.objects.filter(nombre__icontains=q)
    return render(request, 'paraElla.html', {'pro': eventos})

#nos lleva a el
class ConsultarEl(ListView):
    model = Producto
    template_name = 'comercio/paraEl.html'
    context_object_name = 'pro'
    queryset = Producto.objects.filter(tipo='M')

#nos lleva a el
class ConsultarParejas(ListView):
    model = Producto
    template_name = 'comercio/parejas.html'
    context_object_name = 'pro'
    queryset = Producto.objects.filter(tipo='P')




#VA EN EL BOTON DE CARRITO
class AgregarCarrito(CreateView):
    model = Carrito
    form_class = CarritoForm
    template_name = 'comercio/agregar.html'
    success_url = reverse_lazy('comercio:vercar')

    def form_valid(self, form):
        idProd = self.kwargs.get('pk', None)
        carritoProd = Carrito.objects.filter(idPro__id = idProd, idUser = self.request.user.id)
        if (len(carritoProd) != 0):
            carritoProd[0].cantidad += form.cleaned_data['cantidad']
            carritoProd[0].subTotal = carritoProd[0].idPro.precio * carritoProd[0].cantidad
            carritoProd[0].save()
            return redirect('comercio:vercar')
        else:
            self.object = form.save(commit=False) 
            var= Producto.objects.get(pk=self.kwargs.get('pk', None))
            self.object.idPro=var
            subTotal = self.object.cantidad*var.precio
            self.object.subTotal = subTotal
            self.object.idUser = self.request.user.id
            self.object.save()
            return super(AgregarCarrito, self).form_valid(form)



#ELIMINA CADA UNIDAD DE PRODUCTO 
class EliminarProd(DeleteView):
    model = Carrito
    success_url = reverse_lazy('comercio:vercar')  

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

#VEMOS TODOS LOS PRODUCTOS DEL CARRITO
class ConsultarCarrito(ListView):
    model = Carrito
    template_name = 'comercio/carrito.html'

    def get_context_data(self, **kwargs):
        context=super(ConsultarCarrito, self).get_context_data(**kwargs)
        context['pro'] =Carrito.objects.filter(idUser= self.request.user.id)
        context['total'] = Carrito.objects.filter(idUser= self.request.user.id).aggregate(Sum('subTotal')).get('subTotal__sum')
        # context['total'] = round(context['total'],2)
        return context
        if context['total']is not None:
            context['total'] = round(context['total'],2)
        else:
            context['total'] = 0


#VACIAR EL CARRITO DE COMPRA
class Pagar(View):
    model = Carrito
    def get(self, request, *args, **kwargs):
        Carrito.objects.all().delete()
        return redirect('comercio:vercar')

        
class VerFormulario(ListView):
    model = Producto
    template_name = 'comercio/formulario.html'
    