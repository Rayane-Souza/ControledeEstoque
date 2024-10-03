from django.shortcuts import render, redirect
from .mongodb import verify_user


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('senha')
        
        if verify_user(email, password):
            success_message = "Login realizado com sucesso!"
            return render(request, 'home/home.html', {'success_message': success_message})
        else:
            error_message = "Email ou senha inválidos."
            return render(request, 'home/home.html', {'error_message': error_message})

    return render(request, 'home/home.html')


