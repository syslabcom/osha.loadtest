from webunit.utility import Upload
import funkload.Lipsum
import funkload.utils
import os
import tempfile
import webwork.loadtest.base


LIPSUM = funkload.Lipsum.Lipsum()

class medium(webwork.loadtest.base.TestCase):
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
    	* Click - Go to the dark side
    	* Click - Go to a specific workspace
    	* Search for a word/phrase
    	* Filter - narrow down the search results by clicking on "type" checkbox
    	* View the first search result
    	* Logoff
    	"""
        self.login()
        self.get('/stardesk/workspaces?onlymyspaces=true')
        self.assertEllipsis('...Only my spaces...', self.getBody())
        self.get('/stardesk/workspaces/baseline')
        self.assertEllipsis('...baseline...Group by Label...', self.getBody())
        searchterm = 'TestableTextString'
        resp = self.post('/stardesk/workspaces/baseline/starsearch#content', {
                'SearchableText': searchterm,
                'path': '/star/workspaces/baseline',
                })
        self.assertEllipsis('...baseline...%s...' % searchterm, self.getBody())

        resp = self.post('/stardesk/workspaces/baseline/starsearch#content', {
                'SearchableText': searchterm,
                'portal_type': ['Document'],
                'path': '/star/workspaces/baseline',
                })
        self.assertEllipsis('...baseline...%s...' % searchterm, self.getBody())
        self.get('/stardesk/workspaces/baseline/my-doc')
        self.assertEllipsis('...%s...' % searchterm, self.getBody())
        self.logout()

class medium_epp(medium):
    is_epp = True
    
