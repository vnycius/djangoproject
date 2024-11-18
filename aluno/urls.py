from django.urls import path
from . import views 

urlpatterns = [
    path('', views.mensagem_de_sucesso, name='mensagem_de_sucesso'),
]
