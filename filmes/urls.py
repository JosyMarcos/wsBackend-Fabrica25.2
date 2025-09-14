from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_filmes, name='lista_filmes'),
    path('novo/', views.cria_filme, name='cria_filme'),
    path('editar/<int:id>/', views.edita_filme, name='edita_filme'),
    path('deletar/<int:id>/', views.deleta_filme, name='deleta_filme'),
    path('filme-api/<str:titulo>/', views.exibe_filme_api, name='exibe_filme_api'),
]

