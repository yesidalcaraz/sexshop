from django.contrib.auth.models import User#modelos de datos propios de django
from django.contrib.auth.forms import UserCreationForm#nombre formulario que quieres crear y creation form
from django.contrib.auth import login,logout
from django.shortcuts import render
from django.views.generic import CreateView,FormView
from django.urls import reverse_lazy
from .forms import FormularioLogin,FormularioRegistro
from django.http import HttpResponseRedirect


class RegistroUsuario(CreateView):
    model = User
    template_name = 'base.html'
    form_class = FormularioRegistro
    success_url = reverse_lazy('login')#aqui solo se coloca el name donde queremos que nos lleve
    
class Login(FormView):
    model = User
    template_name = 'login.html'
    form_class = FormularioLogin 
    success_url = reverse_lazy('comercio:inicio') 
    
    def dispatch(self,request, *args, **kwargs):#es como una validación
        if request.user.is_authenticated:#si esta autenticado por cliente nos lleve reverse anterior
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args, **kwargs)#cuando Login esta en mayuscula es la clase
            
    def form_valid(self,form):
        login(self.request,form.get_user())#ese metodo lo puedo utilizar pq estoy creando un form view y permite hacer uso de un monton de metodos de la clase form view. y nos retorna el login ya validado                  
        return super(Login,self).form_valid(form)
        #pasa por este metodo y hace la validacion del formulario, crea una variable de funcion con el login de los datos que han sido enviados del usuario y retorna el login completo con la variable creada.
        #el entra en esta clase dos veces cuando pinta el form en el archivo html. Si no va a variable de sesion formulada pues va al else y envia el formulario se va a validar en el def form valid y si es correcto retorna el url reverse lazy
    
def logoutUsuario(request):#definimos la funcion para cerrar la sesion
    logout(request)
    return HttpResponseRedirect('/comercio/')      
    