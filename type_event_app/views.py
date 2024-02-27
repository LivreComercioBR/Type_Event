from django.shortcuts import render, HttpResponse, redirect
from . utils import validar_dados, password_is_valid
from django.contrib import messages, auth
from django.contrib.messages import constants
from .models import User


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        validar_usuario = validar_dados(
            request, username=username, email=email)

        validar_senha = password_is_valid(request,
                                          password=senha, confirm_password=confirmar_senha)

        if not validar_usuario or not validar_senha:
            return redirect('/usuarios/cadastro')

        if validar_usuario and password_is_valid:

            try:
                usuario = User.objects.create_user(
                    username=username,
                    email=email,
                    password=senha,
                )
                usuario.save()
                messages.add_message(
                    request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
                return redirect('/usuarios/logar')
            except:
                messages.add_message(
                    request, constants.ERROR, 'Erro interno do sistema!')
                return redirect('/usuarios/cadastro')


def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/eventos/novo_evento')
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=password)

        if not usuario:
            messages.add_message(request, constants.ERROR,
                                 'Usuário ou senha inválidos!')
            return redirect('/usuarios/logar')
        else:
            auth.login(request, usuario)
            return redirect('/eventos/novo_evento')


def sair(request):
    auth.logout(request)
    return redirect('/usuarios/logar')
