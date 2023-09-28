from django.shortcuts import render
from .models import Cosmonaut
from .forms import CosmonautForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView


# Create your views here.




class CosmonautListView(ListView):
    model = Cosmonaut
    template_name = 'cosmonauts_app/home.html'
    context_object_name = 'cosmonauti'
    paginate_by = 5


def create_cosmonaut(request):
    if request.method == 'POST':
        form = CosmonautForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shows_all_cosmonauts') 
    else:
        form = CosmonautForm()

    return render(request, 'cosmonauts_app/create_cosmonaut.html', {'form': form})


def edit_cosmonaut(request, pk):
    kosmonaut = get_object_or_404(Cosmonaut, pk=pk)

    if request.method == 'POST':
        form = CosmonautForm(request.POST, instance=kosmonaut)
        if form.is_valid():
            form.save()
            return redirect('shows_all_cosmonauts')
    else:
        form = CosmonautForm(instance=kosmonaut)

    return render(request, 'cosmonauts_app/edit_cosmonaut.html', {'form': form})



def delete_cosmonaut(request, pk):
    kosmonaut = get_object_or_404(Cosmonaut, pk=pk)
    if request.method == 'POST':
        kosmonaut.delete()
        return redirect('shows_all_cosmonauts') 
    return render(request, 'cosmonauts_app/delete_cosmonaut_confirm.html', {'kosmonaut': kosmonaut})