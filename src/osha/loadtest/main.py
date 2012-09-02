from funkload.utils import xmlrpc_get_credential, xmlrpc_get_seq
import ConfigParser
import os
import os.path
import pkg_resources
import random
import re
import subprocess
import sys


def run_test():
    exit_code, _ = _run_funkload('funkload.TestRunner')
    sys.exit(exit_code)


def run_benchmark():
    exit_code, config_path = _run_funkload('funkload.BenchRunner')
    _build_report(config_path)
    sys.exit(exit_code)


def _run_funkload(funkload_module):
    module_path, test_method, server_url = sys.argv[1:4]  # XXX parse options

    safe_url = re.sub('[^a-zA-Z0-9]+', '-', server_url.rstrip('/'))
    config_dir = os.path.join('credential-server', safe_url)
    config_file = control_credential_server('start', config_dir)

    cwd = os.getcwd()
    try:
        pkg_dir = pkg_resources.resource_filename(module_path, '')
        os.chdir(pkg_dir)

        module_file = module_path.split('.')[-1] + '.py'
        argv = [module_file, test_method, '--url=' + server_url] + sys.argv[4:]
        os.environ['LOADTEST_CWD'] = cwd
        exit_code = run_as_script(funkload_module, 'main', *argv)

    finally:
        os.chdir(cwd)
        control_credential_server('stop', config_dir, config_file)
        if os.path.isdir(config_dir):
            os.unlink(os.path.join(config_dir, config_file))
            # The credential server may not creating the pid file in time.
            pid_file = os.path.join(config_dir, 'file_credential.pid')
            if os.path.exists(pid_file):
                os.unlink(pid_file)

    test_class = test_method.split('.')[0]
    config_path = os.path.join(pkg_dir, test_class + '.conf')
    return exit_code, config_path


def _build_report(config_path):
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    result_path = config.get('bench', 'result_path')
    run_as_script('funkload.ReportBuilder', 'main', '--html', result_path)


def control_credential_server(command, config_dir, config_file=None,
                              show_output=True):
    cwd = os.getcwd()
    try:
        os.chdir(config_dir)
    except OSError:
        pass
    else:
        if config_file is None:
            config_file = configure_credential_server_port()
        run_as_script('funkload.CredentialFile', 'main',
                      config_file, command, show_output=show_output)
    finally:
        os.chdir(cwd)

    return config_file


def configure_credential_server_port():
    config = ConfigParser.ConfigParser()
    config.read('credential.conf')
    host = config.get('server', 'host')
    port = random.randint(1024, 65535)
    os.environ['LOADTEST_CREDENTIAL_SERVER'] = '%s:%s' % (host, port)
    config_file = 'credential-%s.conf' % port
    config = open('credential.conf')
    config2 = open(config_file, 'w')
    config2.write(config.read() % dict(port=port))
    config2.close()
    return config_file


def get_credentials(group):
    cred_host, cred_port = os.environ[
        'LOADTEST_CREDENTIAL_SERVER'].split(':')
    return xmlrpc_get_credential(cred_host, cred_port, group)


def get_seq():
    cred_host, cred_port = os.environ[
        'LOADTEST_CREDENTIAL_SERVER'].split(':')
    return xmlrpc_get_seq(cred_host, cred_port)


def run_as_script(module, function, *args, **kw):
    options = ({} if kw.get('show_output', True) else
               dict(stdout=subprocess.PIPE, stderr=subprocess.PIPE))
    return subprocess.call([
            sys.executable,
            '-c', """\
import sys
sys.path[:] = %(sys_path)r
sys.argv[0] = 'script'
import %(module)s
%(module)s.%(function)s()
""" % dict(sys_path=sys.path, module=module, function=function)
            ] + list(args), **options)
