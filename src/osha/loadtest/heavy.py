import os, time, random
import osha.loadtest.base
from funkload.utils import xmlrpc_get_seq

    
class heavy(osha.loadtest.base.TestCase):
    group = 'heavyusagegroup'
    chost,cport = os.environ.get('LOADTEST_CREDENTIAL_SERVER').split(':')
    workspaces = []
    
    def setUp(self):
        pass
        
    def setUpBench(self):
        pass

    def tearDown(self):
        pass

    def tearDownBench(self):
        pass

                  
    def test_heavy(self):
        """
        * Login via the main home page URL
        * Logoff
        """


        self.login()
        
        self.logout()


