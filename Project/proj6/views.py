from django.shortcuts import render, redirect
from . models import About_Page
from . forms import AboutForm
# Create your views here.

def list_about(request):
    pages = About_Page.objects.all()
    return render(request, 'about_page.html', {'pages': pages})



def create_about(request):
    form = AboutForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect('list_about')
    return render(request, 'page-form.html', {'form': form})

def update_about(request, id):
    pages = About_Page.objects.get(id=id)
    form = AboutForm(request.POST or None, instance=pages)
    if form.is_valid():
        form.save()
        return redirect('list_about')
    return render(request, 'page-form.html', {'form':form, 'pages':pages})

def delete_about(request, id):
    pages = About_Page.objects.get(id=id)
    if request.method == 'POST':
        pages.delete()
        return redirect('list_about')
    return render(request, 'page-delete-confirm.html', {'pages':pages})