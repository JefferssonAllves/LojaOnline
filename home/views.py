from django.shortcuts import render, redirect
from clientes.models import Cliente
import requests

def home(request):
    if 'cliente' in request.session:
        cliente = request.session.get('cliente')
        context = {
            'nome':cliente['nome'],
        }
        return render(request, './home.html', context)
    return redirect('/login')

def revendedores(request):
    termo_busca = request.GET.get('termo_busca')
    if termo_busca:
        revendedores = Cliente.objects.filter(nome=termo_busca)
    else:
        revendedores = Cliente.objects.all()

    return render(request, './revendedores.html', {'revendedores':revendedores})

def cadastro_revendedor(request):
    url = "https://gist.githubusercontent.com/jonasruth/61bde1fcf0893bd35eea/raw/10ce80ddeec6b893b514c3537985072bbe9bb265/paises-gentilicos-google-maps.json"

    paises = requests.get(url)

    if paises.status_code == 200:
        data = paises.json()
        return render(request, './cadastro_revendedor.html', {'paises':data})
    else:
        print("Erro na requisição:", paises.status_code)

    return render(request, './cadastro_revendedor.html')


def logout(request):
    del request.session['cliente']
    return redirect('/')
