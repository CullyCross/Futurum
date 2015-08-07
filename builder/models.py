from django.db import models
from skills.models import Skill


# todo(CullyCross): add translations

class Field(models.Model):
    class Meta:
        abstract = True

    # Foreign keys
    skill = models.ForeignKey(Skill, related_name='%(class)s_set')

class TextField(Field):

    # Other fields
    data = models.TextField()


class CharField(Field):

    # Other fields
    data = models.CharField(max_length=100)


class ImageField(Field):

    # Other fields
    # data = models.ImageField()
    pass
