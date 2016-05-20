from __future__ import unicode_literals

from django.db import models

from django.conf import settings
User = settings.AUTH_USER_MODEL
# from clubs.models import Club


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.name
