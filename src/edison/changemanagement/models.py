from django.db import models
from django.contrib.auth.models import User
from edison.cmdb.models import ConfigurationItem

# Models for Change Management System
class ChangeHeader(models.Model):
	Title = models.CharField(max_length=255)
	Requestor = models.ForeignKey(User)
	Summary = models.TextField()
	AffectedItems = models.ManyToManyField(ConfigurationItem)
	GitRepoUrl = models.CharField(max_length=255)

	def __unicode__(self):
		return self.Title

	class Meta:
		verbose_name = 'Change Request Header'
		verbose_name_plural = 'Change Request Headers'
		ordering = ['Title']

class Details(models.Model):
	Header = models.ForeignKey(ChangeHeader)
	Description = models.TextField()
	GitCommit = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.Description

	class Meta:
		verbose_name = 'Change Request Detail'
		verbose_name_plural = 'Change Request Details'
		ordering = ['Description']
