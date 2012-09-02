import webwork.loadtest.base


class failure(webwork.loadtest.base.TestCase):

    def test_failure(self):
        self.fail()
