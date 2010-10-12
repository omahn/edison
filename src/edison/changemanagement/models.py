import datetime
from django.db import models
from django.contrib.auth.models import User
from edison.cmdb.models import ConfigurationItem

# Models for Change Management System
class ChangeStatus(models.Model):
	Description = models.CharField(max_length=128)
	ClosesChangeRequest = models.BooleanField()

	def __unicode__(self):
		return self.Description

	class Meta:
		verbose_name = 'Current Status'
		verbose_name_plural = 'Change Statuses'

class ChangeHeader(models.Model):
	Title = models.CharField(max_length=255)
	Requestor = models.ForeignKey(User)
	Summary = models.TextField()
	AffectedItems = models.ManyToManyField(ConfigurationItem)
	GitRepoUrl = models.CharField(max_length=255)
        Created = models.DateField(editable=False)
    	Due = models.DateTimeField()	
	Status = models.ForeignKey(ChangeStatus)
	Completed = models.BooleanField(editable=False)
    
	def save(self):
		if not self.id:
	        	self.created = datetime.date.today()
	        super(ChangeHeader, self).save()

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
	Created = models.DateTimeField()
	UpdatedBy = models.ForeignKey(User)
	
	def save(self):
		if not self.id:
	        	self.created = datetime.date.today()
	        super(ChangeHeader, self).save()

	def __unicode__(self):
		return self.Description

	class Meta:
		verbose_name = 'Change Request Detail'
		verbose_name_plural = 'Change Request Details'
		ordering = ['Description']
