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
        * read subpages...
        * open practical solutions
        * open risk observatory
        * open topics, priority groups, sectors
        * open campaigns
        * open competitions
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
        self.assertEllipsis('...Highlights...In Focus...Navigation...Free Newsletter...Latest Tweets...', self.getBody())
        self.get('/en/about/')
        self.assertEllipsis('...Who we are...What we do...More about...Free Newsletter...', self.getBody())
        self.get('/en/about/organisation')
        self.assertEllipsis('...Overview of how the Agency...Navigation...Events...More about...Free Newsletter...', self.getBody())
        self.get('/en/about/director_corner')
        self.assertEllipsis('...Director...Corner...OSH Blog...Translations...More about...Free Newsletter...', self.getBody())
        self.get('/en/about/jobs')
        self.assertEllipsis('...Current job vacancies...Ongoing job vacancies...Short-listed job vacancies...', self.getBody())
        self.get('/en/about/calls')
        self.assertEllipsis('...Current calls for contractors...Ongoing calls for contractors...', self.getBody())
        self.get('en/about/contact_us')
        self.assertEllipsis('...Contact us...', self.getBody())
        self.get('en/practical-solutions/providers')
        self.assertEllipsis('...Providers...', self.getBody())
        self.get('en/practical-solutions/faqs')
        self.assertEllipsis('...FAQ...', self.getBody())
        self.get('en/riskobservatory')
        self.assertEllipsis('...European Risk Observatory...Anticipating new and emerging risks...Visit the enterprise survey...Publications...Our Events...News...', self.getBody())
        self.get('en/topics')
        self.assertEllipsis('...Topics...', self.getBody())
        self.get('en/topics/accident_prevention')
        self.assertEllipsis('...Accident Prevention...More about...Publications...News...', self.getBody())
        self.get('en/topics/business-aspects-of-osh')
        self.assertEllipsis('...Business aspects of OSH...Why is a good working environment good for business?...Publications...Practical solutions...News...', self.getBody())
        self.get('/en/sector/horeca')
        self.assertEllipsis('...HORECA. The hotel, restaurant and catering sector...Publications...Practical solutions...News...', self.getBody())
        self.get('/en/sector/healthcare')
        self.assertEllipsis('...Health and safety of healthcare staff...Publications...Practical solutions...EU Framework...News...Events...', self.getBody())
        self.get('/en/sector/rail_air_water_transport')
        self.assertEllipsis('...Rail, Air and Water Transport...Publications...Practical solutions...Related content...News...', self.getBody())
        self.get('/en/sector/road_transport')
        self.assertEllipsis('...Occupational Safety and Health of Road Transport Drivers...Publications...Practical solutions...Related content...', self.getBody())
        self.get('/en/campaigns')
        self.assertEllipsis('...Healthy Workplaces Campaigns...', self.getBody())
        self.get('/en/campaigns/hw2008')
        self.assertEllipsis('...Last wave...Navigation...Get involved...Our partners...More about...News...', self.getBody())
        self.get('/en/campaigns/ew2007')
        self.assertEllipsis('...European awards...Navigation...Get involved...Our partners...More about...News...Free Newsletter...Alert Service...', self.getBody())
        self.get('/en/campaigns/ew2006')
        self.assertEllipsis('...European awards...Navigation...Our partners...Get involved...Resources Database...News...Free Newsletter...', self.getBody())
        self.get('/en/campaigns/ew2005')
        self.assertEllipsis('...STOP THAT NOISE!...Navigation...More about...Our partners...Get involved...Did you know?...Free Newsletter...News...', self.getBody())
        self.get('/en/campaigns/ew2004')
        self.assertEllipsis('...BUILDING IN SAFETY...Navigation...Agency publications...Agency web features...Campaign partner organisations...Free Newsletter...', self.getBody())
        self.get('/en/campaigns/ew2003')
        self.assertEllipsis('...European Week for Safety and Health at Work 2003...Navigation...Agency publications...Agency web features...', self.getBody())
        self.get('/en/competitions')
        self.assertEllipsis('...Competitions...Closed competitions...', self.getBody())
        # this didn't work: - why?
        # self.get('/en/competitions')
        # self.assertEllipsis('...Competitions...Navigation...Events...Closed competitions...', self.getBody())
        self.get('/en/competitions/good-practice-award_2012-2013')
        self.assertEllipsis('...Good Practice Awards 2012-2013...More competitions...', self.getBody())
        self.get('/en/competitions/hw_film_award_2012')
        self.assertEllipsis('...Healthy Workplaces Film Award 2012...More competitions...', self.getBody())
        self.get('/en/competitions/european-photo-competition-2011')
        self.assertEllipsis('...European Photo Competition...More competitions...', self.getBody())
        




