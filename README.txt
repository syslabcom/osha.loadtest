=========================
The loadtest distribution
=========================

Load tests for the system.

This package provides two things: a wrapper around `funkload`_ that
encapsulates some if its more annoying usage aspects, and performance tests
for the application.

.. _`funkload`: http://funkload.nuxeo.org/


Installation
============

This package is compatible with Python version 2.7. It can be installed using
either easy_install or the buildout setup that comes with it.


Usage
=====

The loadtest funkload wrapper comes with two scripts you can execute.
The first runs a test method without benchmarking it:

$ bin/run-test PACKAGE.MODULE CLASS.TEST_METHOD APP_URL

For example:

$ bin/run-test loadtest.light light.test_performance http://localhost:7000/star

The test runner leaves behind two log files named as configured for the test
class (CLASS), one plain-text file which contains, among other stuff, the page
contents of error pages, and one XML file.

The benchmark runner takes the exact same arguments:

$ bin/run-benchmark PACKAGE.MODULE CLASS.TEST_METHOD APP_URL

Running this script will produce an XML log file and also create an HTML test
report from it. (This requires gnuplot to be installed.)


Application setup
=================

First, the application needs to be installed using deployment.
Then, in the Plone instance, create two users:

- a Plone user that has the Administrators role

- a Zope manager user outside of Plone (for deleting workspaces via the ZMI)

These need to be listed in the credentials configuration found in
credential-server/http-localhost-7000-star. If you plan to use a different
URL, copy that directory to another subdirectory of credential-server, named
after the URL with any sequence of non-alphanumeric characters replaced by a
dash.

The tests included in this package assume the language of the Plone site to be
English.
