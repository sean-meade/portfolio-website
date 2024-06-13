from django.shortcuts import render
from .models import Project, Tag, ProjectTag
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'home.html')

def projects_tag(request, tag_id):

    tag = Tag.objects.get(id=tag_id)

    projects_tag = ProjectTag.objects.filter(tag = tag)

    projects = Project.objects.filter(id__in=projects_tag)

    tags = Tag.objects.all()

    context = {
                'projects': projects,
                'tags': tags,
                }
    return render(request, 'projects.html', context)

def projects(request):

    projects = Project.objects.order_by('?')
    tags = Tag.objects.all()
    query = None
    tag_ids = None

    if request.GET:

        if 'checks[]' in request.GET:
            # TODO: fix so tags work when clicked
            tag_ids = request.GET.getlist('checks[]')
            project_tags_list = None
            project_tags = Tag.objects.filter(id__in=tag_ids)
            
            projecttags = ProjectTag.objects.filter(tag__in=project_tags)

            projects = Project.objects.filter(id__in=projecttags)
        
        else:
            tag_ids = None
            
        if 'q' in request.GET:
            query = request.GET['q']
            
            if not query or query == "":
                
                context = {
                    'projects': projects,
                    'search_term': None,
                    'tags': tags,
                    'highlight_tags': tag_ids,
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
        'highlight_tags': tag_ids,
    }

    return render(request, 'projects.html', context)
