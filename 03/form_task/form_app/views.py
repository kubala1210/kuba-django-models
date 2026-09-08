from django.shortcuts import render
from django.http import HttpRequest
from .forms import ContactForm


def contact_view(request):
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            success = True
    else:
        form = ContactForm()

    return render(request, "form_app/contact.html", {"form": form, "success": success})

    
    # Create your views here.
