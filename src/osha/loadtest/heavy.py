import os, time, random
import osha.loadtest.base
from funkload.utils import xmlrpc_get_seq
import funkload.Lipsum
LIPSUM = funkload.Lipsum.Lipsum()    

class heavy(osha.loadtest.base.TestCase):
    group = 'heavyusagegroup'
    chost,cport = os.environ.get('LOADTEST_CREDENTIAL_SERVER').split(':')
    workspaces = []
    

                  
    def test_heavy(self):
        """
        * Login via the main home page URL
        * Logoff
        """

        self.login()
        self.assertEllipsis('...You are now logged in...', self.getBody())
        self.get('/en/tmp/')
        self.assertEllipsis('...Contents...View...Edit...', self.getBody())
        self.create_document('myfunkloaddoc')
        self.logout()


