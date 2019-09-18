from django.shortcuts import render, redirect
from . models import Three_Page
from . forms import ThreeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required
def list_three(request):
    pages = Three_Page.objects.all().order_by('-created')
    paginator = Paginator(pages, 1)
    page = request.GET.get('page')
    try:
        ppages = paginator.page(page)
    except PageNotAnInteger:
        ppages = paginator.page(1)
    except EmptyPage:
        ppages = paginator.page(paginator.num_pages)
    return render(request, 'three_page.html', {'pages': pages, 'ppages':ppages})

def create_three(request):
    form = ThreeForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect('list_three')
    return render(request, 'page-form.html', {'form': form})

def update_three(request, id):
    pages = Three_Page.objects.get(id=id)
    form = ThreeForm(request.POST or None, instance=pages)
    if form.is_valid():
        form.save()
        return redirect('list_three')
    return render(request, 'page-form.html', {'form':form, 'pages':pages})

def delete_three(request, id):
    pages = Three_Page.objects.get(id=id)
    if request.method == 'POST':
        pages.delete()
        return redirect('list_three')
    return render(request, 'page-delete-confirm.html', {'pages':pages})

