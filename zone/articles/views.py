from django.shortcuts import render

# Create your views here.
# http://127.0.0.1:8000

def ds(request):
    return render(request, 'articles/ds.html')

def ai(request):
    return render(request, 'articles/ai.html')

def ml(request):
    return render(request, 'articles/ml.html')

def dl(request):
    return render(request, 'articles/dl.html')