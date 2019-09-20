from django.shortcuts import render, redirect
from . models import Home_Page
from . forms import HomeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import sitemaps
from django.urls import reverse


# Create your views here.

def list_home(request):
    pages = Home_Page.objects.all().order_by('-created')
    paginator = Paginator(pages, 1)
    page = request.GET.get('page')
    try:
        ppages = paginator.page(page)
    except PageNotAnInteger:
        ppages = paginator.page(1)
    except EmptyPage:
        ppages = paginator.page(paginator.num_pages)
    return render(request, 'home_page.html', {
        'pages': pages,
        'ppages': ppages
    })


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changfreq = 'daily'

    def items(self):
        return ['list_home']

    def location(self, item):
        return reverse(item)


def error_404(request, data):
    data = {}
    return render(request,'error_404.html', data)

def error_500(request):
    return render(request,'error_500.html')




def create_home(request):
    form = HomeForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect('list_home')
    return render(request, 'page-form.html', {'form': form})

def update_home(request, id):
    pages = Home_Page.objects.get(id=id)
    form = HomeForm(request.POST or None, instance=pages)
    if form.is_valid():
        form.save()
        return redirect('list_home')
    return render(request, 'page-form.html', {'form':form, 'pages':pages})

def delete_home(request, id):
    pages = Home_Page.objects.get(id=id)
    if request.method == 'POST':
        pages.delete()
        return redirect('list_home')
    return render(request, 'page-delete-confirm.html', {'pages':pages})
