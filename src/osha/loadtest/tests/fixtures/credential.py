import webwork.loadtest.base


class credential(webwork.loadtest.base.TestCase):

    def test_credential(self):
        self.assertEqual(['bar', 'baz'], self.get_credentials('foo'))
