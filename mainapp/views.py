from django.shortcuts import render

def index(request):
    context = {'username': 'юрий', 'array': [1, 2, 3, 4, 5]}
    return render(request, 'mainapp/index.html', context=context)

# def main(request):
#     return render(request, 'mainapp/main.html')

# def products(request):
#     return render(request, 'mainapp/products.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')

def catalog(request):
    return render(request, 'mainapp/catalog.html')

