from django.shortcuts import render
from .forms import Form

# Create your views here.

def contact(request):

    if request.method == 'POST':
        form = Form(request.POST)

        if form.is_valid():
            form.save()

    form = Form()
    return render(request, 'contact/contact.html', {'form': form})

