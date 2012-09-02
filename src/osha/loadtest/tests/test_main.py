import os
import os.path
import pkg_resources
import shutil
import socket
import tempfile
import unittest
import webwork.loadtest.main


class Base(unittest.TestCase):

    show_loadtest_output = False

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        shutil.copytree(
            pkg_resources.resource_filename(
                'webwork.loadtest', 'tests/fixtures/credential-server'),
            os.path.join(self.tmpdir, 'credential-server'))
        self.cwd = os.getcwd()
        os.chdir(self.tmpdir)

    def tearDown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.tmpdir)

    def run_as_script(self, test_method, *args):
        return webwork.loadtest.main.run_as_script(
            'webwork.loadtest.main', test_method, *args,
            show_output=self.show_loadtest_output)


class RunTest(Base):

    def test_smoke(self):
        self.run_as_script(
            'run_test',
            'webwork.loadtest.tests.fixtures.smoke',
            'smoke.test_smoke',
            'http://fixture.example.com/smoke',
            )
        self.assertEqual(
            ['credential-server', 'smoke-test.log', 'smoke-test.xml'],
            sorted(os.listdir('.')))

    def test_credential_server(self):
        credential_config = os.path.join(
            'credential-server', 'http-fixture-example-com-credential')
        files = set(os.listdir(credential_config))
        self.assertEqual(0, self.run_as_script(
                'run_test',
                'webwork.loadtest.tests.fixtures.credential',
                'credential.test_credential',
                'http://fixture.example.com/credential',
                ))
        self.assertEqual(files.union(('file_credential.log',)),
                         set(os.listdir(credential_config)))

    def test_failing_test_runs_exit_with_nonzero(self):
        self.assertEqual(1, self.run_as_script(
                'run_test',
                'webwork.loadtest.tests.fixtures.failure',
                'failure.test_failure',
                'http://fixture.example.com/failure',
                ))

    def test_credential_server_config_dir_is_normalised(self):
        self.assertEqual(0, self.run_as_script(
                'run_test',
                'webwork.loadtest.tests.fixtures.credential',
                'credential.test_credential',
                'http://fixture.example.com/credential',
                ))
        self.assertEqual(0, self.run_as_script(
                'run_test',
                'webwork.loadtest.tests.fixtures.credential',
                'credential.test_credential',
                'http://fixture.example.com/credential/',
                ))


class RunBenchmark(Base):

    def test_smoke(self):
        self.run_as_script(
            'run_benchmark',
            'webwork.loadtest.tests.fixtures.smoke',
            'smoke.test_smoke',
            'http://fixture.example.com/smoke',
            )
        expected = set([
                'credential-server', 'smoke-bench.log', 'smoke-bench.xml'])
        names = set(os.listdir('.'))
        self.assertTrue(expected.issubset(names))
        self.assertEqual(1, len(names - expected))
        report_dir = (names - expected).pop()
        self.assertTrue(report_dir.startswith('test_smoke-'))


class CredentialServer(Base):

    show_output = False

    def tearDown(self):
        webwork.loadtest.main.control_credential_server(
            'stop',
            'credential-server/http-fixture-example-com-credential',
            self.config_file,
            show_output=self.show_output)
        del self.config_file
        super(CredentialServer, self).tearDown()

    def test_start_stop(self):
        with self.assertRaises(KeyError):
            webwork.loadtest.main.get_credentials('foo')
        self.config_file = webwork.loadtest.main.control_credential_server(
            'start',
            'credential-server/http-fixture-example-com-credential',
            show_output=self.show_output)
        self.assertEqual(
            ['bar', 'baz'], webwork.loadtest.main.get_credentials('foo'))
        webwork.loadtest.main.control_credential_server(
            'stop',
            'credential-server/http-fixture-example-com-credential',
            self.config_file,
            show_output=self.show_output)
        with self.assertRaises(socket.error):
            webwork.loadtest.main.get_credentials('foo')
