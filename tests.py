# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
from models import Company
from django.test import TestCase
from django.test.client import Client

class CompanyAddressTest(TestCase):
    fixtures = ['fixtures/cmdb_fixtures.json']

    def setUp(self):
        # Setup the client 
        client = Client()
 
    def test_response(self):
        # get the index page
        response = self.client.get('/accounts/login/',{'username':'admin','password':'password'})

	# Check we have recieved a '200' response
	self.failUnlessEqual(response.status_code,200)

