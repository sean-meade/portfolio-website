from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Project, Tag, ProjectTag
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

    if request.GET:

        if 'checks[]' in request.GET:
            # TODO: fix so tags work when clicked
            tags = request.GET.getlist('checks[]')
            project_tags = None
            for tag in tags:
                project_tags_list = Tag.objects.filter(tag_name=tag)
                print("project_tags_list: ", project_tags_list)
                project_tags = project_tags | project_tags_list
                print("project_tags: ", project_tags)
            projecttags = ProjectTag.objects.filter(tag_id__in=project_tags)
            projects = Project.objects.filter(id__in=project_tags)
            
            print("projects: ", projects)

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
