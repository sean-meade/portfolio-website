from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=40)
    website = models.URLField(max_length = 200)
    github = models.URLField(max_length = 200)
    # Number of characters = max_length (meaning if I want all tiles to be the same I can't have styling or find another way)
    description = models.TextField(max_length = 500)
    # TODO: Set up uplaod to and retrievable from cloudinary
    image = CloudinaryField('image')
    collaboration = models.BooleanField(default=False)
    under_construction = models.BooleanField(default=False)

    def get_tags(self):
        projecttags = ProjectTag.objects.filter(project=self)
        tags = Tag.objects.filter(id__in=projecttags.values_list('tag'))

        return tags
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    class Meta:
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=30)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ProjectTag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)