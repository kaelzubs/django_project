from django.shortcuts import render, redirect
from . models import Five_Page
from . forms import FiveForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
def list_five(request):
    pages = Five_Page.objects.all().order_by('-created')
    paginator = Paginator(pages, 1)
    page = request.GET.get('page')
    try:
        ppages = paginator.page(page)
    except PageNotAnInteger:
        ppages = paginator.page(1)
    except EmptyPage:
        ppages = paginator.page(paginator.num_pages)
    return render(request, 'five_page.html', {'pages': pages, 'ppages':ppages})

def create_five(request):
    form = FiveForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect('list_five')
    return render(request, 'page-form.html', {'form': form})

def update_five(request, id):
    pages = Five_Page.objects.get(id=id)
    form = FiveForm(request.POST or None, instance=pages)
    if form.is_valid():
        form.save()
        return redirect('list_five')
    return render(request, 'page-form.html', {'form':form, 'pages':pages})

def delete_five(request, id):
    pages = Five_Page.objects.get(id=id)
    if request.method == 'POST':
        pages.delete()
        return redirect('list_five')
    return render(request, 'page-delete-confirm.html', {'pages':pages})

