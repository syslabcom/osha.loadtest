import os, time, random
import webwork.loadtest.base
from funkload.utils import xmlrpc_get_seq

from base import NUMWS
    
class heavy2(webwork.loadtest.base.TestCase):
    is_epp = False
    group = 'heavyusagegroup'
    chost,cport = os.environ.get('WEBWORK_LOADTEST_CREDENTIAL_SERVER').split(':')
    workspaces = []
    
    def setUp(self):
        pass
        
    def setUpBench(self):
        pass

    def tearDown(self):
        pass

    def tearDownBench(self):
        pass

                  
    def test_heavy2(self):
        """
        * Login via the main home page URL
        * Click - Go to the dark side
        * Click - Go to a specific workspace
        * Upload a document
        * Subscribe to the document/folder
        * Delete that same document
        * Unsubscribe to the document/folder
        * Click on the workspace calendar icon
        * Click on full calendar
        * Create an event (fill in all required fields)
        * Save the event
        * Delete the same event
        * Logoff
        """

#        seq = xmlrpc_get_seq(self.chost,self.cport) % NUMWS
        seq = self.thread_id % NUMWS

        self.get('/')
        self.assertEllipsis('...Latest publications...', self.getBody())

        self.login()
        
        self.workspace = '/stardesk/workspaces/baseline-%0.2d' % seq
        
        self.get('/stardesk/workspaces')
        self.assertEllipsis('...Only my spaces...', self.getBody())

        self.get(self.workspace)
        self.assertEllipsis('...baseline...Group by Label...', self.getBody())

        self.get(self.workspace+'/@@context-settings')
        #if "Unsubscribe from changes" in self.getBody():
        #    self.get(self.workspace+'/@@unsubscribe')
        #    self.get(self.workspace+'/@@context-settings')
        #    #self.assertEllipsis('...Subscribe to changes...', self.getBody())
        #else:
        self.get(self.workspace+'/@@subscribe?notifiers:list=mail')
        self.get(self.workspace+'/@@context-settings')
            #self.assertEllipsis('...Unsubscribe from changes...', self.getBody())

        filename = self.create_file('myfile.bin')
        self.get(self.workspace+'/myfile.bin')
        #self.get(self.workspace+'/myfile.bin/@@context-settings')
        #self.get(self.workspace+'/myfile.bin/@@subscribe?notifiers:list=mail')
        #self.get(self.workspace+'/myfile.bin/@@context-settings')
        #self.get(self.workspace+'/myfile.bin/@@unsubscribe')
#        self.delete_file(self.workspace+'/myfile.bin')
        
        self.get(self.workspace+'/@@context-settings')
        # temporary measure while test is stopping in between
        #if "Unsubscribe from changes" in self.getBody():
        self.get(self.workspace+'/@@unsubscribe')
        self.get(self.workspace+'/@@context-settings')
            #self.assertEllipsis('...Subscribe to changes...', self.getBody())
        #else:
        #    self.get(self.workspace+'/@@subscribe?notifiers:list=mail')
        #    self.get(self.workspace+'/@@context-settings')
            #self.assertEllipsis('...Unsubscribe from changes...', self.getBody())

        # Calendar
        self.get(self.workspace+'/project_calendar')
        self.assertEllipsis('...Upcoming events...', self.getBody())

        self.get(self.workspace+'/project-fullcalendar.html')
        self.assertEllipsis('...Year View...', self.getBody())
        
        # create event
        #self.create_event('my-event')
        #self.get('my-event')
        #self.delete_event()

        # create newsitem
	self.create_document('my-info')
	self.get('my-info')
	self.delete_object(self.workspace+'/my-info')

        # do the contacts export here, as we don't get a cookie for plone in these NFT
        self.get('/stardesk/dashboard')
        
        self.get('/stardesk/contacts')

        self.get('/stardesk/contacts/@@contact-list?userid=ealtiyaprak%40thy.com&submit=submit&sortby=surname%2Cfullname&groups=ASA+Members&searchterm=&airline-filter=')
        self.get('/stardesk/contacts/@@contact-csv?submit=submit&page_size=-1&sortby=surname%2Cfullname&groups=ASA+Members&searchterm=&airline-filter=')
        self.logout()


class heavy2_epp(heavy2):
    is_epp = True
