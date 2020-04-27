from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **Kwargs):
        super(FormularioLogin, self).__init__(*args,**Kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class FormularioRegistro(UserCreationForm): 
    class Meta: 
        model= User
        fields = ['first_name', 'last_name', 'username','email']
        labels = {
            'first_name': 'Nombre del usuario',
            'last_name': 'Indica apellido',
            'username': 'Indica username',
            'email': 'Indica email',
        }
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control','id':'nombre'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','id':'apellido'}),
            'username': forms.TextInput(attrs={'class':'form-control','id':'username'}),
            'email': forms.TextInput(attrs={'class':'form-control','id':'email'}),
        }