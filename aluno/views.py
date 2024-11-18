from django.shortcuts import render
from django.http import HttpResponse 

def mensagem_de_sucesso(request):
    return HttpResponse("Atividade Realizada com muito Sucesso!")
