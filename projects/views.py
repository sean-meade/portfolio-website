from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Project, Tag
from django.db.models import Q
import sys

# Create your views here.
def home(request):
    return render(request, 'home.html')

def projects(request):

    projects = Project.objects.all()
    tags = Tag.objects.all()
    query = None
    tag = None

    print(request.GET.getlist('checks[]'))
    print(request.__dict__, file=sys.stderr)

    if request.GET:

        if 'checks[]' in request.GET:
            # TODO: fix so tags work when clicked
            tag = request.GET.getlist('checks[]')
            projects = Project.objects.filter(projecttag__friendly_name__in=tag)
            print("projects: ", projects)
            tag = Tag.objects.filter(friendly_name__in=tag)
            print("tag: ", tag)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('projects'))

            queries = Q(
                name__icontains=query) | Q(
                description__icontains=query)
            projects = projects.filter(queries)

    context = {
        'projects': projects,
        'search_term': query,
        'current_tag': tag,
        'tags': tags,
    }

    return render(request, 'projects.html', context)