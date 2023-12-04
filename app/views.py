from django.shortcuts import render
from django.http.request import HttpRequest
from app.forms import Contact_form
from .models import Contact_model, create


# Create your views here.
def index(request):
    return render(request, "index.html")


def contact(request):
    form = Contact_form()
    if request.GET:
        form = Contact_form(request.GET)
        if form.is_valid():
            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            email = form.cleaned_data['email']
            create(name, number, email)

            return render(request, 'contact.html', {'form': form, 'name': name, 'number': number, 'email': email})

    else:
        return render(request, "contact.html")
