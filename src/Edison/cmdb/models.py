from django.db import models
from django.contrib.auth.models import User

# These are the models required for the basic CMDB

# First, Define our list of countries
class Country(models.Model):
    CountryName = models.CharField(max_length=255)
    CountryCode = models.CharField(max_length=3)

    def __unicode__(self):
        return self.CountryCode

    
    
# Now define the counties/States that we can use
class County(models.Model):
    CountyName = models.CharField(max_length=128)
    CountyCountry = models.ForeignKey('Country')
    
    def __unicode__(self):
        return self.CountyName

# Where do people/things live?
class Address(models.Model):
    AddressLineOne = models.CharField(max_length=128)
    AddressLineTwo = models.CharField(max_length=128)
    AddressLineThree = models.CharField(max_length=128)
    AddressPostcode = models.CharField(max_length=15)
    AddressCounty = models.ForeignKey('County')
    AddressCountry = models.ForeignKey('Country') 

    def __unicode__(self):
        return u'%s, %s, %s' % (self.AddressLineOne, self.AddressCounty, self.AddressPostcode)

# What companies are there that we might want to talk to?
class Company(models.Model):
    CompanyName = models.CharField(max_length=255)
    CompanyHeadOffice = models.ForeignKey('Address')
    CompanySupportNumber = models.CharField(max_length=50)
    CompanySupportEmail = models.EmailField()
    CompanyAddress = models.ForeignKey('Address')
    
    def __unicode__(self):
        return self.CompanyName
    
# A list of all our contacts both within and external to the company we work for
class Contact(models.Model):
    TITLE_CHOICES = (
                     'Mr',
                     'Mrs',
                     'Miss',
                     'Ms',
                     )
    ContactTitle = models.CharField(max_length=6,choices=TITLE_CHOICES)
    ContactFirstName = models.CharField(max_length=128)
    ContactLastName = models.CharField(max_length=128)
    ContactPrimaryPhone = models.CharField(max_length=50)
    ContactEmailAddress = models.EmailField()
    ContactCompany = models.ForeignKey('Company')
    
    def __unicode__(self):
        return u'%s %s %s' % (self.ContactTitle, self.ContactFirstName, self.ContactLastName)

    
# Our Datacentres
class DataCentre(models.Model):
    DataCentreName = models.CharField(max_length=255)
    DataCentreShortCore = models.CharField(max_length=10)
    DataCentreAddress = models.ForeignKey('Address')
    DataCentrePrincipleContact = models.ForeignKey('Contact')

    def __unicode__(self):
        return self.DataCentreShortCode

# The rooms in the datacentres
class DataCentreRoom(models.Model):
    DataCentreRoomName = models.CharField(max_length=25)
    DataCentre = models.ForeignKey('DataCentre')
    
    def __unicode__(self):
        return u'%s in %s' % (self.DataCentreRoomName, self.DataCentre)
    
# The suites in the datacentres
class DataCentreSuite(models.Model):
    DataCentreSuiteName = models.CharField(max_length=128)
    DataCentreRoom = models.ForeignKey('DataCentreRoom')
    
    def __unicode__(self):
        return u'%s -> %s' % (self.DataCentreSuiteName, self.DataCentreRoom)

# The racks in the suites in the rooms in the datacentres....
class DataCentreRack(models.Model):
    DataCentreRackName = models.CharField(max_length=25)
    DataCentreRoom = models.ForeignKey('DataCentreRoom',blank=True)
    DataCentreSuite= models.ForeignKey('DataCentreSuite',blank=True)
    
    def __unicode__(self):
        return u'%s -> %s (%s)' % (self.DataCentreRackName, self.DataCentreSuite, self.DataCentreRoom)

# The different classes of configuration items
class ConfigurationItemClass(models.Model):
    ConfigurationItemClassName = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.ConfigurationItemClassName

# The configuration items (servers/switches etc)
class ConfigurationItems(models.Model):
    ConfigurationItemHostname = models.CharField(max_length=255)
    ConfigurationItemRack = models.ForeignKey('DataCentreRack')
    ConfigurationItemAsset = models.CharField(max_length=128)
    ConfigurationItemSupportTag = models.CharField(max_length=128)
    ConfigurationItemOwner = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.ConfigurationItemHostname
    
# The network interfaces that are assigned to configuration items
class NetworkInterfaces(models.Model):
    NetworkInterfaceName = models.CharField(max_length=5)
    NetworkInterfaceMacAddress = models.CharField(max_length=30)
    NetworkInterfaceIPAddress = models.IPAddressField()
    ConfigurationItem = models.ForeignKey('ConfigurationItem')