from webunit.utility import Upload
import funkload.Lipsum
import funkload.utils
import os
import tempfile
import osha.loadtest.base
import random

LIPSUM = funkload.Lipsum.Lipsum()


class admin(osha.loadtest.base.TestCase):
    group = 'adminusagegroup'
    
    def setUp(self):
        pass
        
    def setUpBench(self):
        pass

    def tearDown(self):
        pass

    def tearDownBench(self):
        pass
        
    def test_admin(self):
        """ Implements the following admin usage steps
            * Login to Redhat site (or integrated Plone when ready?)
        	* Search for a user
        	* Change that user's password
        	* For this user, delete membership from 1 group
        	* Add user back into the same group
        	* Logoff
	    """
        username, password = self.get_credentials(self.group)
	    

