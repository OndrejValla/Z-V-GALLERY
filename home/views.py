from django.shortcuts import render
from products.models import Project

def index(request):
    """ A view to return the index page / home page """


    projects = Project.objects.all()

    context = {
        'projects': projects,
        }
    return render(request, 'home/index.html', context)
