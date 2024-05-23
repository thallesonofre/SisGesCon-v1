#Criar esse aquivo no app para incluir, tirar, personalizar os campos  do form
#exemplo colocar o email obrigatorio
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    # evita cadastro de emails repetidos ou para validar dados
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('O email {} já está em uso!'.format(email))
        
        return email