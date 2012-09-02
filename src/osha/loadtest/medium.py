from webunit.utility import Upload
import funkload.Lipsum
import funkload.utils
import os
import tempfile
import osha.loadtest.base


LIPSUM = funkload.Lipsum.Lipsum()

class medium(osha.loadtest.base.TestCase):
    is_epp = False
    group = 'mediumusagegroup'


    def setUp(self):
        pass
        
    def setUpBench(self):
        pass

    def tearDown(self):
        pass

    def tearDownBench(self):
        pass

    def test_medium(self):
        """ Implements the following medium usage steps
    	* Login via the main home page URL
    	* Logoff
    	"""
        self.login()
        self.logout()

