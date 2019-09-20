from django.shortcuts import render, redirect
from . models import Contact_Page
from . forms import ContactForms, ContactForm
from django.core.mail import send_mail, get_connection


# Create your views here.

def list_contact(request):
    pages = Contact_Page.objects.all()
    submitted = False
    if request.method == 'POST':
        form = ContactForms(request.POST or None )
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.smtp.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['donmart4u@gmail.com'],
                connection=con
                )
            return redirect('contact_success')
    else:
            form = ContactForms()
            if 'submitted' in request.GET:
                submitted = True
    return render(request,'contact_page.html', {'form': form, 'pages': pages, 'submitted': submitted})


def contact_success(request):
    return render(request, 'contact_success.html')


def create_contact(request):
    form = ContactForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect('list_contact')
    return render(request, 'page-form.html', {'form': form})

def update_contact(request, id):
    pages = Contact_Page.objects.get(id=id)
    form = ContactForm(request.POST or None, instance=pages)
    if form.is_valid():
        form.save()
        return redirect('list_contact')
    return render(request, 'page-form.html', {'form':form, 'pages':pages})

def delete_contact(request, id):
    pages = Contact_Page.objects.get(id=id)
    if request.method == 'POST':
        pages.delete()
        return redirect('list_contact')
    return render(request, 'page-delete-confirm.html', {'pages':pages})



