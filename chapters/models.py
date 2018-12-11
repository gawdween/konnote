# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from subjects.models import Subject
from django.contrib.auth.models import User
from levels.models import Level
from django.conf import settings


class Chapter(models.Model):
    subject = models.ForeignKey(Subject, default='')
    level = models.ForeignKey(Level, default='')
    name = models.CharField(max_length=100, default='')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.subject.name + ' | ' + self.level.name + ' | ' + self.name

#  This class is not linked to any other entity and therefore, does not need a field of any other type in this class