from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Cliente

def login(request):
    if 'cliente' in request.session:
        return redirect('home')
    if request.method == 'POST':
        cliente = Cliente.objects.filter(email=request.POST.get('clie_email'))
        if cliente.exists():
            cliente = cliente.get()
            if cliente.senha == request.POST.get('clie_senha'):
                print(Cliente.objects.all())
                request.session['cliente'] = cliente.get_atributtes()
                return redirect('/home', {'cliente' : cliente})
        return render(request, './login.html', {'msg':'erro'})
    return render(request, './login.html')

def registro(request):
    if request.method == "POST":
        nome = request.POST['clie_nome']
        email = request.POST['clie_email']
        senha = request.POST['clie_senha']

        cliente = Cliente.objects.filter(email=email)

        if cliente.exists():
            return redirect('login')

        cliente = Cliente(
            nome=nome,
            email=email,
            senha=senha,
            grupo='cliente',
        )

        cliente.save()
        return redirect('login')
    return render(request, './registro.html', {'msg':'registrado'})

def esqueceu_senha(request):
    if request.method == 'POST':
        if request.POST.get('clie_email'):
            if request.POST.get('clie_nova_senha'):
                cliente = Cliente.objects.get(email=request.POST.get('clie_email'))
                cliente.senha = request.POST.get('clie_nova_senha')
                cliente.save()
                return redirect('/')
            else:
                return render(request, './esqueceu-senha.html', {'msg':'POST', 'clie_email':request.POST.get('clie_email')})
    return render(request, './esqueceu-senha.html')

