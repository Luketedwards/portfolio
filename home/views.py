from django.shortcuts import render
from projects.models import Project, comments
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .utilities import send_email

# Create your views here.

def index(request):
    """ A view to return the index page """
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'home/index.html', context)

def process_contact_form(request):
    """ A view to process the contact form """
    if request.method == 'POST':
        form_data = {
            'name': request.POST['name'],
            
            'email': request.POST['email'],
            'subject': request.POST['subject'],
            'message': request.POST['message'],
        }
        
        
        send_email(form_data)
        messages.success(request, 'Your message has been sent!')
        return redirect(reverse('home'))
        
    else:
        redirect(reverse('home'))

    return render(request, template, context)