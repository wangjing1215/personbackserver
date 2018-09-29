# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(u'name', max_length=256)
	password = models.TextField(u'password')
	email = models.CharField(u'name', max_length=30)
	is_staff = models.CharField(u'name', max_length=30)
	def __unicode__(self):
		return self.name