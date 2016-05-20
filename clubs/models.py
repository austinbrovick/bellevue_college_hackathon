from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from tags.models import Tag


User = settings.AUTH_USER_MODEL

def upload_location(instance, filename):
    print "******* in upload function *************"
    location = str(instance.name)
    instance.url = "%s/%s" %(location, filename)
    return "clubs/%s/%s" %(location, filename)



class Club(models.Model):
    president = models.OneToOneField(User)
    name = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    club_picture = models.ImageField(upload_to=upload_location, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)


    def __unicode__(self):
        return self.name

