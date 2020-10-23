from django.shortcuts import render, redirect
from .models import Contacs
from .forms import ContacsForm
from django.views.generic import DetailView

def contact_home(request):
    contact = Contacs.objects.all()
    return render(request, 'contact/detail.html', {'contact': contact})

def list_go(request):
    all_of_list = Contacs.objects.all()
    return render(request, 'contact/list.html', {'all_of_list': all_of_list})

class ContactDetailView(DetailView):
    model = Contacs
    template_name = 'contact/details_view.html'
    context_object_name = 'article'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ContacsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = 'Форма была неверной'

    form = ContacsForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'contact/create.html', data)