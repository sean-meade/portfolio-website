from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Project, Tag, ProjectTag
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'home.html')

def projects(request):

    projects = Project.objects.all()
    tags = Tag.objects.all()
    query = None

    print(request.GET.getlist('checks[]'))

    if request.GET:

        if 'checks[]' in request.GET:
            # TODO: fix so tags work when clicked
            tag_ids = request.GET.getlist('checks[]')
            project_tags_list = None
            for tag_id in tag_ids:
                project_tag = Tag.objects.filter(id=tag_id)
                print("project_tag: ", project_tag)
                if project_tags_list == None:
                    project_tags_list = project_tag
                else:
                    project_tags_list = project_tags_list | project_tag
                print("project_tags_list: ", project_tags_list)
            
            projecttags = ProjectTag.objects.filter(tag__in=project_tags_list).values_list('project')
            print("projecttags: ", projecttags)

            projects = Project.objects.filter(id__in=projecttags)
            
            print("projects: ", projects)

        if 'q' in request.GET:
            query = request.GET['q']
            print('query: ', query == "")
            if not query or query == "":
                print("hits here")
                context = {
                    'projects': projects,
                    'search_term': query,
                    'tags': tags,
                }
                return render(request, 'projects.html', context)

            queries = Q(
                name__icontains=query) | Q(
                description__icontains=query)
            projects = projects.filter(queries)

    context = {
        'projects': projects,
        'search_term': query,
        'tags': tags,
    }

    return render(request, 'projects.html', context)
