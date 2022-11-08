from django.shortcuts import render, redirect
from .models import Project, comments
from .forms import ProjectForm
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.
@csrf_exempt
def addProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
            image = form.cleaned_data.get('image')
            image.save()
    else:
        form = ProjectForm()
        form.fields['date'].initial = datetime.datetime.now()
    return render(request, 'projects/addProject.html', {'form': form})


def portfolio_details(request, pk):
    """ A view to return the index page """
    project = Project.objects.get(pk=pk)
    
    context = {
        'project': project,
        
    }
    return render(request, 'projects/portfolio-details.html', context)