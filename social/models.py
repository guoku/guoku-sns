from django.db import models
from django.contrib.auth import get_user_model

from model_utils import managers


class SocailQuerySet(models.query.QuerySet):

    def blocked(self):
        return self.filter(blocked=True)


class Social(models):
    owner =  models.ForeignKey(get_user_model(), related_name='user')
    following = models.ForeignKey(get_user_model(), related_name='following')
    blocked = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = managers.PassThroughManager.for_queryset_class(SocailQuerySet)()

    class Meta:
        ordering = ['-timestamp']


    def timesince(self, now=None):
        from django.utils.timesince import timesince as timesince_
        return timesince_(self.timestamp, now)


    def set_blocked(self):
        self.blocked = True

    def set_unbloced(self):
        self.blocked = False

__author__ = 'edison'
