from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from tags.models import Tag
User = settings.AUTH_USER_MODEL

GRADES = (
    ('Running Start', 'Running Start'),
    ('Freshman', 'Freshman'),
    ('Sophomore', 'Sophomore'),
    ('Junior', 'Junior'),
    ('Senior', 'Senior')
    )

MAJORS = (
    ('Finance', 'Finance'),
    ('Accounting', 'Accounting'),
    ('Marketing', 'Marketing'),
    ('Human Resources', 'Human Resources'),
    ('Economics', 'Economics'),
    ('Computer Science', 'Computer Science'),
    ('English', 'English'),
    ('History', 'History'),
    )

def upload_location(instance, filename):
    print "******* in upload function *************"
    location = str(instance.user.id)
    instance.url = "%s/%s" %(location, filename)
    return "users/%s/%s" %(location, filename)

class Profile(models.Model):
    user = models.OneToOneField(User)
    club = models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to=upload_location, null=True, blank=True)
    grade = models.CharField(max_length=30, choices=GRADES, null=True, blank=True)
    major = models.CharField(max_length=30, choices=MAJORS, null=True, blank=True)
    tags = models.ManyToManyField(Tag)



    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        url = reverse("profile", kwargs={"username" : self.user.username})
        return url
