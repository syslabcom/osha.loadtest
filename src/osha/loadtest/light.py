import funkload.utils
import os
import webwork.loadtest.base


class light(webwork.loadtest.base.TestCase):

    group = 'lightusagegroup'
    is_epp = False

    def setUp(self):
        pass
        
    def setUpBench(self):
        pass

    def tearDown(self):
        pass

    def tearDownBench(self):
        pass
        
    def test_light(self):
        """
        * Login
        * Click on a workspace's direct URL
        * Download a document
        * Logoff
        """
        self.login()
        self.get('/')
        self.assertEllipsis(
            '...About...Members...Dashboard...', self.getBody())
        self.get('/stardesk/workspaces/baseline')
        self.assertEllipsis('...baseline...', self.getBody())
        self.get('/stardesk/workspaces/baseline/my-doc')
        self.assertEllipsis('...Dummy content follows...', self.getBody())
        self.logout()


class light_epp(light):
    is_epp = True
