import funkload.utils
import os
import osha.loadtest.base


class light(osha.loadtest.base.TestCase):

    group = 'lightusagegroup'
    is_epp = False

    def setUp(self):
        pass
        
    def setUpBench(self):
        pass

    def tearDown(self):
        pass

    def tearDownBench(self):
        pass
        
    def test_light(self):
        """
        * open homepage
        * open about section
        * read subpages
        * open practical solutions
        * open risk observatory
        * open topics, priority groups, sectors
        * open campaigns
        * opn competitions
        * open press
        * open publications
        * open organisations
        * open oshnetwork
        * open legislation
        * open safety and health in figures
        * open seminary
        * perform a search for "accident"
        """
        self.get('/en/')
        self.assertEllipsis(
            '...Navigation...Highlights...In Focus...Free Newsletter...Latest Tweets...', self.getBody())
        self.get('/en/about/')
        self.assertEllipsis('...WHo we are...What we do...', self.getBody())


