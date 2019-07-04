from django.shortcuts import render

def index(request):
    return render(request, 'mainapp/index.html')

# def main(request):
#     return render(request, 'mainapp/main.html')
#
# def products(request):
#     return render(request, 'mainapp/products.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')

def catalog(request):
    return render(request, 'mainapp/catalog.html')

