from django.shortcuts import render, redirect
from .forms import LeadForm


# Create your views here.
def index(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bienvenida')
        else:
            form = LeadForm()
            return render(request, 'myapp/index.html', {'form': form})
    else:
        form = LeadForm()
        return render(request, 'myapp/index.html', {'form': form})


def bienvenida(request):
    return render(request, 'myapp/bienvenida.html', {})
