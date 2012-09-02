from webunit.utility import Upload
import tempfile
from funkload.FunkLoadTestCase import FunkLoadTestCase
import funkload.Lipsum
from funkload.utils import Data
from gocept.testing.assertion import Ellipsis, Exceptions
import os
import os.path
import urlparse
import webwork.loadtest.main
import random

LIPSUM = funkload.Lipsum.Lipsum()
NUMWS = 40

class TestCase(FunkLoadTestCase, Ellipsis, Exceptions):

    def __init__(self, *args, **kw):
        FunkLoadTestCase.__init__(self, *args, **kw)
        # XXX any customizations needed?

        self.server_url = self.conf_get('main', 'url')
        if not self.server_url.endswith('/'):
            self.server_url += '/'
        self.last_url = ''
        self.addHeader('Accept-language', 'en')

    # The following properties are meant to ensure that in whatever way
    # funkload sets the path of the log files, they don't end up among the
    # source files but rather in the current working directory of the user
    # before starting the load test run, provided the test runner exports that
    # directory to the environment (webwork.loadtest.main.run_test() does).
    # Otherwise, they will end up among the source according to funkload's
    # default behaviour.

    @property
    def log_path(self):
        cwd = os.environ.get('WEBWORK_LOADTEST_CWD', '')
        return os.path.join(cwd, os.path.basename(self._log_path))

    @log_path.setter
    def log_path(self, value):
        self._log_path = value

    @property
    def result_path(self):
        cwd = os.environ.get('WEBWORK_LOADTEST_CWD', '')
        return os.path.join(cwd, os.path.basename(self._result_path))

    @result_path.setter
    def result_path(self, value):
        self._result_path = value

    def _log_response(self, response, rtype, description, time_start,
                      time_stop, log_body=False):
        # hack to log HTTP errors
        if log_body:
            self.logi('HTTP error in ' + response.url + '\n' + response.body)
        return FunkLoadTestCase._log_response(
            self, response, rtype, description,
            time_start, time_stop, log_body)

    def relative_to_portal(self, path):
        if path.startswith('/'):
            return self.server_url + path[1:]
        else:
            return urlparse.urljoin(self.last_url, path)

    def get(self, path, **kw):
        result = super(TestCase, self).get(
            self.relative_to_portal(path), **kw)
        self.last_url = self.getLastUrl()
        return result

    def post(self, path, data, **kw):
        result = super(TestCase, self).post(
            self.relative_to_portal(path), data, **kw)
        self.last_url = self.getLastUrl()
        return result

    def getLastUrl(self):
        return urlparse.urljoin(
            self.server_url, super(TestCase, self).getLastUrl())

    def get_credentials(self, group):
        return webwork.loadtest.main.get_credentials(group)

    def get_sequence(self):
        return webwork.loadtest.main.get_seq()

    def setUp(self):
        pass 
        if not self.in_bench_mode:
            self.setUpBench()

    def tearDown(self):
        pass
        #if not self.in_bench_mode:
        #    self.tearDownBench()

    def setUpBench(self):
        self.workspaces = []
        self.login()


        self.get('/stardesk/workspaces')
        spaces = self.getBody()
        
        if 'baseline' not in spaces:
            self.create_workspace('baseline')
            self.__class__.workspace = self.last_url
            self.create_document('my-doc')
            self.__class__.document = self.last_url.replace('/view', '/')
            self.edit_document()
        
        for i in range(NUMWS):
            ws_name = "baseline-%0.2d" %i
            if ws_name not in spaces:
                self.create_workspace(ws_name)

        self.logout()
            
            
    def tearDownBench(self):
        pass
        #if self.workspaces:
        #    self.login('manager')
        #    self.delete_workspaces(self.workspaces)

    def delete_workspaces(self, ids):
        id_param = [('ids:list', x) for x in ids]
        self.post(
            '/stardesk/workspaces', id_param + [('manage_delObjects:method', 'Delete')])
#        for id in ids:
#            self.assertNotIn(id, self.getBody())

    def login(self, group=None):
        if group is None:
            group = self.group
        username, password = self.get_credentials(group)
#        if self.is_epp:
#            resp = self.post(self.server_url + "portal/login",
#               {'username': username,
#                    'password': password,
#                    'initialURI': '/portal/dologin'})
        #else:
        resp = self.post('/stardesk/login_form', {
                '__ac_name': username,
                '__ac_password': password,
                'form.submitted': '1',
                'submit': 'Login'})
        self.assertEllipsis(
            '...Dashboard...', self.getBody())

    def logout(self):
        if self.is_epp:
            self.get('/portal/staralliance/profile?portal:componentId=UIPortal&portal:action=Logout')
        else:
            self.get('/stardesk/logout')

    def create_workspace(self, name):
        self.get('/stardesk/workspaces/++add++staralliance.types.workspace')
        self.post('/stardesk/workspaces/++add++staralliance.types.workspace', {
                'title': name,
                'redirect': '#',
                'submit': 'submit'})
        self.assertEllipsis(
            '...Stardesk...baseline...', self.getBody())
        workspace_id = filter(None, self.getLastUrl().rsplit('/'))[-1]
        self.workspaces.append(workspace_id)

    def create_document(self, name):
        self.get('++add++Document')
        self.post('++add++Document', {
                'title': name,
                'redirect': 'view',
                'submit': 'submit'})
	self.last_url = self.last_url.replace('/view', '')
        self.assertEllipsis(
            '...%s...' % name, self.getBody())

    def edit_document(self):
        self.get('edit')
        self.post('edit', {
                'text': 'TestableTextString' + LIPSUM.getMessage(),
                'submit': 'submit'}, ok_codes=[204])
        # XXX check that it worked?

    def delete_document(self):
        document = self.last_url
        self.get('delete_confirmation')
        auth = funkload.utils.extract_token(
            self.getBody(), 'name="_authenticator" value="', '"')
        self.post('delete_confirmation', {
                'form.submitted': '1',
                'submit': 'Delete',
                '_authenticator': auth,
                })
        self.get(document, ok_codes=[404])


    def create_file(self, name):
        self.get(self.workspace)
        self.get(self.workspace+"/@@quick_upload_init") 
        
        filename = '/tmp/%s' % name
        self.addCleanup(os.unlink, filename)
        with open(filename, 'w') as output:
            output.write('Dummy content follows:\n\n' + LIPSUM.getMessage())
        
        self.post(self.workspace+"/@@quick_upload_file", { 
            'qqfile': Upload(filename),
	    'typeupload': 'File'
                 })
        self.last_url = self.last_url.replace('/view', '')
        return filename

    def download_file(self, name):
        self.get(name)
        self.assertEllipsis('Dummy content follows...', self.getBody())


    def delete_object(self, url=''):
        if not url:
	    url = self.last_url
	pe = url.split('/')
	parent = '/'.join(pe[:-1])
	id = pe[-1]
	self.get('%s/manage_delObjects?ids:list=%s' % (parent, id))
        self.get(url, ok_codes=[404])

    def delete_file(self, url=''):
        if not url:
	    url = self.last_url
        #self.get(url+'/delete_confirmation')
        #auth = funkload.utils.extract_token(
        #    self.getBody(), 'name="_authenticator" value="', '"')
        #self.post(url+'/delete_confirmation', {
        #        'form.submitted': '1',
        #        'submit': 'Delete',
        #        '_authenticator': auth,
        #        })
	pe = url.split('/')
	parent = '/'.join(pe[:-1])
	id = pe[-1]
	self.get('%s/manage_delObjects?ids:list=%s' % (parent, id))
        self.get(url, ok_codes=[404])


    def create_event(self, name):
        self.get('++add++VSEvent')
        day = random.randint(1,28)
        month = random.randint(1,12)
        hour = random.randint(8,18)
        self.post('++add++VSEvent', {
                'title': name,
                'description': 'testableEventDescription',
                'startDate-day': day,
                'startDate-month': month,
                'startDate-year': '2012',
                'startDate-hour': hour,
                'startDate-minute': '00',
                'endDate-day': day,
                'endDate-month': month,
                'endDate-year': '2012',
                'endDate-hour': hour+2,
                'endDate-minute': '00',
                'location': LIPSUM.getWord(),
                'redirect': 'view',
                'submit': 'submit'})
        self.last_url = self.last_url.replace('/view', '')
        self.assertEllipsis(
            '...%s...' % name, self.getBody())

    delete_event = delete_file



