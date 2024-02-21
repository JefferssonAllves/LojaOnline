from django.shortcuts import render

# Create your views here.
def produtos(request):
    aba_atual = request.GET.get('categoria')
    context = {}
    if aba_atual == 'cubos_magicos':
        context = {'aba':'Cubos Mágicos', 'teste':range(4), 'img':'https://m.media-amazon.com/images/I/61hiK7uy1EL._AC_SX679_.jpg'}
    elif aba_atual == 'iphones':
        context = {'aba':'Iphones', 'teste':range(4), 'img':'https://m.media-amazon.com/images/I/41Zbbl4P+LL._AC_SX679_.jpg'}
    elif aba_atual == 'carros':
        context = {'aba':'Carros', 'teste':range(4), 'img':'https://res.cloudinary.com/driveau/vehicles/showrooms/models/nissan-gt-r.jpg'}

#NAO PRECISA DESSE MONTE DE IF E ELIF, BASTA SO FILTRAR OBJETOS DO TIPO PRODUTO PELO NOME DA ABA
    return render(request, './produtos.html', context=context )

def teste(request):
    return render(request, './teste.html')