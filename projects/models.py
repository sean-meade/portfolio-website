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


class Tag(models.Model):
    name = models.CharField(max_length=30)


class ProjectTag(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT)
    tag_id = models.ForeignKey(Tag, on_delete=models.PROTECT)