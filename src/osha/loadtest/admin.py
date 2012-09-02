from webunit.utility import Upload
import funkload.Lipsum
import funkload.utils
import os
import tempfile
import webwork.loadtest.base
import random

LIPSUM = funkload.Lipsum.Lipsum()


class admin_epp(webwork.loadtest.base.TestCase):
    is_epp = True
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
        	* Go to Contact list - filter to show all members in the ASA group
        	* Export these members to local desktop
        	* Logoff
	    """
        username, password = self.get_credentials(self.group)
	    
        resp = self.post(self.server_url + "portal/login",
           {'username': username,
            'password': password,
            'initialURI': '/portal/dologin'})
    
        self.get(self.server_url + 'portal/staralliance/group')
        self.assertEllipsis('...Group Management...', self.getBody())

        self.get(self.server_url + 'portal/staralliance/group?portal:componentId=26eda587-6aa8-4e92-bed9-b5e8908e5663&interactionstate=JBPNS_rO0ABXdkAAJvcAAAAAEACVZpZXdDaGlsZAAIb2JqZWN0SWQAAAABABBVSVVzZXJNYW5hZ2VtZW50AAt1aWNvbXBvbmVudAAAAAEAFVVJT3JnYW5pemF0aW9uUG9ydGxldAAHX19FT0ZfXw**&portal:type=action&ajaxRequest=true')
        self.assertEllipsis('...Search:...', self.getBody())
        
        self.post(self.server_url + 'portal/staralliance/group?portal:componentId=26eda587-6aa8-4e92-bed9-b5e8908e5663&interactionstate=JBPNS_rO0ABXcoAAt1aWNvbXBvbmVudAAAAAEADFVJU2VhcmNoRm9ybQAHX19FT0ZfXw**&portal:type=action&ajaxRequest=true',
            {'formOp': 'QuickSearch',
             'searchTerm': 'nftdummy@syslab.com',
             'searchOption': 'userName'})
        self.assertEllipsis('...nftdummy@syslab.com...', self.getBody())

        self.get(self.server_url + 'portal/staralliance/group?portal:componentId=26eda587-6aa8-4e92-bed9-b5e8908e5663&interactionstate=JBPNS_rO0ABXdgAAJvcAAAAAEADFZpZXdVc2VySW5mbwAIb2JqZWN0SWQAAAABABNuZnRkdW1teUBzeXNsYWIuY29tAAt1aWNvbXBvbmVudAAAAAEAC1VJTGlzdFVzZXJzAAdfX0VPRl9f&portal:type=action&ajaxRequest=true')
        self.assertEllipsis('...Change Password:...', self.getBody())
        
        newpw = 'Dummytester$2012-%s' % random.randint(1000,9999)
        self.post(self.server_url + 'portal/staralliance/group?portal:componentId=26eda587-6aa8-4e92-bed9-b5e8908e5663&interactionstate=JBPNS_rO0ABXcmAAt1aWNvbXBvbmVudAAAAAEAClVJVXNlckluZm8AB19fRU9GX18*&portal:type=action&ajaxRequest=true', 
            {'formOp': 'Save',
                'currentSelectedTab':'UIAccountEditInputSet',
                'userName':'nftdummy@syslab.com',
                'changePassword':'true',
                'newPassword':newpw,
                'confirmPassword':newpw,
                'firstName':'NFT',
                'lastName':'Dummy',
                'gender':'male',
                'title':'Test User',
                'approvedBy':'webworkadmin@staralliance.com',
                'emailPrivate':'',
                'user.status':'',
                'interests':'',
                'airlineCode':'',
                'postalAddress':'',
                'postalStreet':'',
                'postalCode':'',
                'postalCity':'Munich',
                'postalCountry':'75',
                'telephoneNumberDirect':'+498930635890',
                'telephoneNumberMobile':'',
                'telephoneNumberFacsimile':'',
                'telephoneNumberTwentyFourHours':''
            })
        
        self.get(self.server_url + 'portal/staralliance/group?portal:componentId=_1128010&portal:action=Close&ajaxRequest=true')

        # back to group management
        # Production
        self.get(self.server_url + 'portal/staralliance/group?portal:componentId=26eda587-6aa8-4e92-bed9-b5e8908e5663&interactionstate=JBPNS_rO0ABXdaAAJvcAAAAAEACkNoYW5nZU5vZGUACG9iamVjdElkAAAAAQAJL3BsYXRmb3JtAAt1aWNvbXBvbmVudAAAAAEAEVRyZWVHcm91cEV4cGxvcmVyAAdfX0VPRl9f&portal:type=action&ajaxRequest=true')
        self.get(self.server_url + 'portal/staralliance/group?portal:componentId=26eda587-6aa8-4e92-bed9-b5e8908e5663&interactionstate=JBPNS_rO0ABXdnAAJvcAAAAAEACkNoYW5nZU5vZGUACG9iamVjdElkAAAAAQAWL3BsYXRmb3JtL05GVFRlc3RHcm91cAALdWljb21wb25lbnQAAAABABFUcmVlR3JvdXBFeHBsb3JlcgAHX19FT0ZfXw**&portal:type=action&ajaxRequest=true')
        
        self.assertEllipsis('...NFTTestGroup...nftdummy...', self.getBody())
        # delete
#        self.addHeader('Cache-control', 'no-cache')
#        self.addHeader('Pragma', 'no-cache')
        self.get('/portal/staralliance/group?portal:componentId=26eda587-6aa8-4e92-bed9-b5e8908e5663&interactionstate=JBPNS_rO0ABXd4AAJvcAAAAAEABEVkaXQACG9iamVjdElkAAAAAQAxbWVtYmVyOm5mdGR1bW15QHN5c2xhYi5jb206L3BsYXRmb3JtL05GVFRlc3RHcm91cAALdWljb21wb25lbnQAAAABAA1VSVVzZXJJbkdyb3VwAAdfX0VPRl9f&portal:type=action&ajaxRequest=true')
#        self.assertNotIn('nftdummy', self.getBody())
        
        self.post(self.server_url + 'portal/staralliance/group?portal:componentId=26eda587-6aa8-4e92-bed9-b5e8908e5663&interactionstate=JBPNS_rO0ABXcxAAt1aWNvbXBvbmVudAAAAAEAFVVJR3JvdXBNZW1iZXJzaGlwRm9ybQAHX19FT0ZfXw**&portal:type=action&ajaxRequest=true',
            dict(formOp='Save', username='nftdummy@syslab.com', membership='member'))
        
        self.assertEllipsis('...NFTTestGroup...nftdummy...', self.getBody())
        
        # logout
        self.get('/portal/staralliance/profile?portal:componentId=UIPortal&portal:action=Logout')

