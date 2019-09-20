from django.shortcuts import render, redirect
from . models import Disclaim_Page
from . forms import DisclaimForm
# Create your views here.

def list_disclaim(request):
    pages = Disclaim_Page.objects.all()
    return render(request, 'disclaimer_page.html', {'pages': pages})

def create_disclaim(request):
    form = DisclaimForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect('list_disclaim')
    return render(request, 'page-form.html', {'form': form})

def update_disclaim(request, id):
    pages = Disclaim_Page.objects.get(id=id)
    form = DisclaimForm(request.POST or None, instance=pages)
    if form.is_valid():
        form.save()
        return redirect('list_disclaim')
    return render(request, 'page-form.html', {'form':form, 'pages':pages})

def delete_disclaim(request, id):
    pages = Disclaim_Page.objects.get(id=id)
    if request.method == 'POST':
        pages.delete()
        return redirect('list_disclaim')
    return render(request, 'page-delete-confirm.html', {'pages':pages})
