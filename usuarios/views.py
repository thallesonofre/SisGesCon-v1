from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
#tem que importar o .forms do fomularia personalizado criado no app
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Perfil



class UsuarioCreate(CreateView):
    template_name = "usuarios/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
    
    # define em que grupo o usuário vai pertencer
    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Plebeu")
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        
        #colocar essa parte apenas se for criar um perfil para o usuário
        Perfil.objects.create(usuario=self.object)
        
        return url
    
        #para renomear titulo e botão
    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args ,**kwargs)
        
        context["titulo"] = "Registro de novo usuário"
        context["botao"] = "Registrar"
        
        return context
    

#cria esse view apenas se for add perfil de usuário    
class PerfilUpdate(UpdateView):
    template_name = 'usuarios/form.html'
    model = Perfil
    fields = ['nome_completo', 'cpf', 'telefone']
    success_url = reverse_lazy('inicio')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object
    
    #para renomear titulo e botão
    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args ,**kwargs)
        
        context["titulo"] = "Meu perfil"
        context["botao"] = "Atualizar"
        
        return context
        