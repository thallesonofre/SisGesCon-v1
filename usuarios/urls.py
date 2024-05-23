from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, PerfilUpdate


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
            template_name='usuarios/login.html'
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('coringa/', UsuarioCreate.as_view(), name='coringa'),
    path('atualizar_perfil/', PerfilUpdate.as_view(), name='atualizar_perfil'),
]
