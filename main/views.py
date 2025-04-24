from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def history(request):
    return render(request, 'history.html')

def frameworks(request):
    return render(request, 'frameworks.html')

def libraries(request):
    return render(request, 'libraries.html')

def documentation(request):
    return render(request, 'documentation.html')
