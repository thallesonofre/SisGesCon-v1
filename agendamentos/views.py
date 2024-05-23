from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .models import Paciente, Procedimento, Agenda


class AgendaListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Agenda
    
    #quebra de pagina
    paginate_by = 5
    
    # consulta no html por data/ou etc no input no caso data
    def get_queryset(self):
        
        txt_data = self.request.GET.get('data')
        
        if txt_data:
            agenda = Agenda.objects.filter(data__icontains=txt_data)
        else:
            agenda = Agenda.objects.all()
            
        return agenda
    
    # para ver apenas os objetos criados por profissional
    def get_queryset(self):
        self.object_list = Agenda.objects.filter(profissional=self.request.user)
        return self.object_list
            
    
class AgendaCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Agenda
    fields = ['data', 'inicio_atendimento', 'nome_paciente', 'tipo_consulta', 'valor_consulta']
    success_url = reverse_lazy("agenda_list")
    
    # preenccher o profissional automáticamente
    def form_valid(self, form):
        # antes do super criar o objeto
        form.instance.profissional = self.request.user
        url = super().form_valid(form)
        # depois do super o objeto é criado
        return url
    
    
class AgendaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Agenda
    fields = ['data', 'inicio_atendimento', 'nome_paciente', 'tipo_consulta', 'valor_consulta', 'fim_atendimento']
    success_url = reverse_lazy("agenda_list")
    
    # para editar apenas os objetos criados por profissional/usuario logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Agenda, pk=self.kwargs['pk'], profissional=self.request.user)
        return self.object
    
    
class AgendaDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Agenda
    success_url = reverse_lazy("agenda_list")
    
    # para excluir apenas os objetos criados por profissional/usuario logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Agenda, pk=self.kwargs['pk'], profissional=self.request.user)
        return self.object
    
    
class AgendaCompleteView(View):
    def get(self, request, pk):
        agenda = get_object_or_404(Agenda, pk=pk)
        agenda.fim_sessao()
        return redirect("agenda_list")
    
    
class PacienteListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Paciente
    
    # para ver apenas os objetos criados por cadastrado_por
    def get_queryset(self):
        self.object_list = Paciente.objects.filter(cadastrado_por=self.request.user)
        return self.object_list


class PacienteCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Paciente
    fields = ['data_cadastro','nome_paciente', 'idade', 'telefone', 'edereco']
    success_url = reverse_lazy("paciente_list")
    
    # preenccher o cadastrado_por automáticamente
    def form_valid(self, form):
        # antes do super criar o objeto
        form.instance.cadastrado_por = self.request.user
        url = super().form_valid(form)
        # depois do super o objeto é criado
        return url
    
    
class PacienteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Paciente
    fields = ['data_cadastro', 'nome_paciente', 'idade', 'telefone', 'edereco']
    success_url = reverse_lazy("paciente_list")
    
    # para editar apenas os objetos criados por cadastrado_por/usuario logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Paciente, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return self.object
    
    
class PacienteDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Paciente
    success_url = reverse_lazy("paciente_list")
    
    # para deletar apenas os objetos criados por cadastrado_por/usuario logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Paciente, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return self.object
    
    
class ProcedimentoListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Procedimento


class ProcedimentoCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Procedimento
    fields = ['nome_procedimento','valor_procedimento']
    success_url = reverse_lazy("procedimento_list")
    
    
class ProcedimentoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Procedimento
    fields = ['nome_procedimento','valor_procedimento']
    success_url = reverse_lazy("procedimento_list")


class ProcedimentoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Procedimento
    success_url = reverse_lazy("procedimento_list")
    

