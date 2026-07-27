from django.http import HttpResponse

def catalogo_produtos(request):
    return HttpResponse("<h1>Catálogo de Produtos</h1><p>Bem-Vindo ao nosso catálogo!</p>")
