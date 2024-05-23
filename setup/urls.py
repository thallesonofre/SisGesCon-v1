from django.contrib import admin
from django.urls import path, include
from agendamentos.views import AgendaListView, AgendaCreateView, AgendaUpdateView, AgendaDeleteView, AgendaCompleteView, PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView, ProcedimentoListView, ProcedimentoCreateView, ProcedimentoUpdateView, ProcedimentoDeleteView
from paineis.views import Home, Index
import usuarios.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(usuarios.urls)),
    
    path('inicio', Home.as_view(), name="inicio"),
    path('', Index.as_view(), name="index"),
    
    path('agenda', AgendaListView.as_view(), name="agenda_list"),
    path('paciente', PacienteListView.as_view(), name="paciente_list"),
    path('procedimento', ProcedimentoListView.as_view(), name="procedimento_list"),
    
    path('create', AgendaCreateView.as_view(), name="agenda_create"),
    path('create_paciente', PacienteCreateView.as_view(), name="paciente_create"),
    path('create_procedimento', ProcedimentoCreateView.as_view(), name="procedimento_create"),
    
    path('update/<int:pk>', AgendaUpdateView.as_view(), name="agenda_update"),
    path('update_paciente/<int:pk>', PacienteUpdateView.as_view(), name="paciente_update"),
    path('update_procedimento/<int:pk>', ProcedimentoUpdateView.as_view(), name="procedimento_update"),
    
    path('delete/<int:pk>', AgendaDeleteView.as_view(), name="agenda_delete"),
    path('delete_paciente/<int:pk>', PacienteDeleteView.as_view(), name="paciente_delete"),
    path('delete_procedimento/<int:pk>', ProcedimentoDeleteView.as_view(), name="procedimento_delete"),
    
    path('complete/<int:pk>', AgendaCompleteView.as_view(), name="agenda_complete"),
    
    
    
    
    
    
    
    
    
    
]
