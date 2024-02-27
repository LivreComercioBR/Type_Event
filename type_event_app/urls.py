from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar'),
    path('sair/', views.sair, name='sair'),
    path('meus_certificados/', views.meus_certificados, name='meus_certificados'),
    
]
