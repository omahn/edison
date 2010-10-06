from django.db import models
from django.contrib.auth.models import User

# These are the models required for the basic CMDB

# First, Define our list of countries
class Country(models.Model):
    CountryName = models.CharField(max_length=255)
    CountryCode = models.CharField(max_length=3)

    def __unicode__(self):
        return self.CountryCode
    
    class Meta:
        #permissions = ()
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['CountryName']
    
    
# Now define the counties/States that we can use
class County(models.Model):
    CountyName = models.CharField(max_length=128)
    CountyCountry = models.ForeignKey('Country')
    
    def __unicode__(self):
        return self.CountyName
    
    class Meta:
        #permissions = ()
        verbose_name = 'County'
        verbose_name_plural = 'Counties'
        ordering = ['CountyName']

# Where do people/things live?
class Address(models.Model):
    AddressLineOne = models.CharField(max_length=128)
    AddressLineTwo = models.CharField(max_length=128,blank=True)
    AddressLineThree = models.CharField(max_length=128,blank=True)
    AddressPostcode = models.CharField(max_length=15)
    AddressCounty = models.ForeignKey('County')
    AddressCountry = models.ForeignKey('Country') 

    def __unicode__(self):
        return u'%s, %s, %s' % (self.AddressLineOne, self.AddressCounty, self.AddressPostcode)
    
    class Meta:
        #permissions = ()
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        ordering = ['AddressLineOne']

# What companies are there that we might want to talk to?
class Company(models.Model):
    CompanyName = models.CharField(max_length=255)
    CompanyHeadOffice = models.ForeignKey('Address')
    CompanySupportNumber = models.CharField(max_length=50)
    CompanySupportEmail = models.EmailField()
        
    def __unicode__(self):
        return self.CompanyName
    
    class Meta:
        #permissions = ()
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['CompanyName']
    
# A list of all our contacts both within and external to the company we work for
class Contact(models.Model):
    TITLE_CHOICES = (
                     ('Mr','Mr'),
                     ('Mrs','Mrs'),
                     ('Miss','Miss'),
                     ('Ms','Ms')
                     )
    ContactTitle = models.CharField(max_length=6,choices=TITLE_CHOICES)
    ContactFirstName = models.CharField(max_length=128)
    ContactLastName = models.CharField(max_length=128)
    ContactPrimaryPhone = models.CharField(max_length=50)
    ContactEmailAddress = models.EmailField()
    ContactCompany = models.ForeignKey('Company')
    
    def __unicode__(self):
        return u'%s %s %s' % (self.ContactTitle, self.ContactFirstName, self.ContactLastName)
    
    class Meta:
        #permissions = ()
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['ContactFirstName']

    
# Our Datacentres
class DataCentre(models.Model):
    DataCentreName = models.CharField(max_length=255)
    DataCentreShortCode = models.CharField(max_length=10)
    DataCentreAddress = models.ForeignKey('Address')
    DataCentrePrincipleContact = models.ForeignKey('Contact')

    def __unicode__(self):
        return self.DataCentreShortCode
    
    class Meta:
        #permissions = ()
        verbose_name = 'Data Centre'
        verbose_name_plural = 'Data Centres'
        ordering = ['DataCentreName']

# The rooms in the datacentres
class DataCentreRoom(models.Model):
    DataCentreRoomName = models.CharField(max_length=25)
    DataCentre = models.ForeignKey('DataCentre')
    
    def __unicode__(self):
        return u'%s in %s' % (self.DataCentreRoomName, self.DataCentre)
    
    class Meta:
        #permissions = ()
        verbose_name = 'Data Centre Room'
        verbose_name_plural = 'Data Centre Rooms'
        ordering = ['DataCentreRoomName']
    
# The suites in the datacentres
class DataCentreSuite(models.Model):
    DataCentreSuiteName = models.CharField(max_length=128)
    DataCentreRoom = models.ForeignKey('DataCentreRoom')
    
    def __unicode__(self):
        return u'%s -> %s' % (self.DataCentreSuiteName, self.DataCentreRoom)
    
    class Meta:
        #permissions = ()
        verbose_name = 'Data Centre Suite'
        verbose_name_plural = 'Data Centre Suites'
        ordering = ['DataCentreSuiteName']

# The racks in the suites in the rooms in the datacentres....
class DataCentreRack(models.Model):
    DataCentreRackName = models.CharField(max_length=25)
    DataCentreRoom = models.ForeignKey('DataCentreRoom',blank=True)
    DataCentreSuite= models.ForeignKey('DataCentreSuite',blank=True)
    
    def __unicode__(self):
        return u'%s -> %s (%s)' % (self.DataCentreRackName, self.DataCentreSuite, self.DataCentreRoom)
    
    class Meta:
        #permissions = ()
        verbose_name = 'Data Centre Rack'
        verbose_name_plural = 'Data Centre Racks'
        ordering = ['DataCentreRackName']

# The different classes of configuration items
class ConfigurationItemClass(models.Model):
    ConfigurationItemClassName = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.ConfigurationItemClassName
    
    class Meta:
        #permissions = ()
        verbose_name = 'Configuration Item Class'
        verbose_name_plural = 'Configuration Item Classes'
        ordering = ['ConfigurationItemClassName']

# The configuration items (servers/switches etc)
class ConfigurationItem(models.Model):
    ConfigurationItemHostname = models.CharField(max_length=255)
    ConfigurationItemRack = models.ForeignKey('DataCentreRack')
    ConfigurationItemAsset = models.CharField(max_length=128)
    ConfigurationItemSupportTag = models.CharField(max_length=128)
    ConfigurationItemOwner = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.ConfigurationItemHostname
    
    class Meta:
        #permissions = ()
        verbose_name = 'Configuration Item'
        verbose_name_plural = 'Configuration Items'
        ordering = ['ConfigurationItemHostname']
        
# The network interfaces that are assigned to configuration items
class NetworkInterfaces(models.Model):
    NetworkInterfaceName = models.CharField(max_length=5)
    NetworkInterfaceMacAddress = models.CharField(max_length=30)
    NetworkInterfaceIPAddress = models.IPAddressField()
    ConfigurationItem = models.ForeignKey('ConfigurationItem')
    
    def __unicode__(self):
        return self.NetworkInterfaceName    
    
    class Meta:
        #permissions = ()
        verbose_name = 'Network Interface'
        verbose_name_plural = 'Network Interfaces'
        ordering = ['NetworkInterfaceName']