from django import forms
from proyectoApp.models import Area
from django.contrib.auth.models import User



class LoginSupervisorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

        labels = {
            'username': 'Codigo Empleado',
            'password': 'Contraseña',
        }

        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':"Codigo Empleado"}),
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':"Contraseña"})
        }

#Formulario del login controlador
class LoginControladorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

        labels = {
            'username': 'Codigo Empleado',
            'password': 'Contraseña',
        }

        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':"Codigo Empleado"}),
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':"Contrase"})
        }
