# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

# This should be only one line. If it must be multi-line, indent the second
# line onwards to keep the PKG-INFO file format intact.
"""Load tests for the system.
"""

from setuptools import setup, find_packages
import glob
import os.path


def project_path(*names):
    return os.path.join(os.path.dirname(__file__), *names)


setup(
    name='osha.loadtest',
    version='0.1.dev0',

    install_requires=[
        'distribute',
        'funkload',
        'gocept.testing',
        ],

    extras_require={
        'test': [
            ],
        },

    entry_points={
        'console_scripts': [
            'run-test=osha.loadtest.main:run_test',
            'run-benchmark=osha.loadtest.main:run_benchmark',
            ],
        },

    author='gocept <mail@gocept.com>',
    author_email='mail@gocept.com',
    license='ZPL 2.1',
    url='https://projects.gocept.com/projects/osha-loadtest/',

    keywords='',
    classifiers="""\
License :: OSI Approved :: Zope Public License
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 2 :: Only
"""[:-1].split('\n'),
    description=__doc__.strip(),
    long_description='\n\n'.join(open(project_path(name)).read() for name in (
            'README.txt',
            'CHANGES.txt',
            )),

    namespace_packages=['osha'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    data_files=[('', glob.glob(project_path('*.txt')))],
    zip_safe=False,
    )
