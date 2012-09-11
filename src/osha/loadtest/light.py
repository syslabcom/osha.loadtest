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
        self.get('en/practical-solutions')
        self.assertEllipsis('...Practical Solutions...Online interactive Risk Assessment tool...', self.getBody())
        self.get('en/practical-solutions/useful-links')
        self.assertEllipsis('...Useful Links...Online interactive Risk Assessment tool...', self.getBody())
        self.get('en/practical-solutions/risk-assessment-tools')
        self.assertEllipsis('...Risk Assessment Tools...', self.getBody())
        self.get('en/practical-solutions/case-studies')
        self.assertEllipsis('...Case Studies...', self.getBody())
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
        self.get('en/topics/change')
        self.assertEllipsis('...Changing World of Work...Publications...News...Events...', self.getBody())
        self.get('en/topics/ds')
        self.assertEllipsis('...Dangerous Substances...More about...Publications...Our Events...News...', self.getBody())
        self.get('en/topics/osheducation')
        self.assertEllipsis('...OSH and education: start young - stay safe...Publications...News...Events...', self.getBody())
        self.get('en/topics/maintenance')
        self.assertEllipsis('...Maintenance...Publications...Practical solutions...Our Events...Visit our special contents...News...', self.getBody())
        self.get('en/topics/msds')
        self.assertEllipsis('...Musculoskeletal disorders...More about...Publications...News...', self.getBody())
        self.get('en/topics/msds/FAQs')
        self.assertEllipsis('...Frequently Asked Questions...Musculoskeletal Disorders: General questions...General Information...', self.getBody())
        self.get('en/topics/noise')
        self.assertEllipsis('...Noise at work...Publications...News...', self.getBody())
        self.get('en/topics/riskassessment')
        self.assertEllipsis('...Risk assessment...Publications...Online interactive Risk Assessment tool...More about...News...Events...', self.getBody())
        self.get('en/topics/stress')
        self.assertEllipsis('...Stress...More about...Publications...Our Events...News...', self.getBody())
        self.get('en/topics/cleaning_workers')
        self.assertEllipsis('...Cleaning workers...Publications...Practical solutions...Our Events...Videos...Research Links...', self.getBody())
        self.get('en/topics/whp')
        self.assertEllipsis('...Workplace Health Promotion...Publications...Practical solutions...In Focus...News...Events...', self.getBody())
        self.get('en/topics/economic-incentives')
        self.assertEllipsis('...Economic Incentives...Publications...Our Events...Scientific articles...News...', self.getBody())
        self.get('en/priority_groups')
        self.assertEllipsis('...Priority Groups...', self.getBody())
        # self.get('en/priority_groups/disability')  
        # self.assertEllipsis('...People with disabilities...More about...Publications...Latest Resources...Events...', self.getBody())
        self.get('en/priority_groups/disability/faq.php')
        self.assertEllipsis('...Frequently Asked Questions...', self.getBody())
        self.get('en/priority_groups/migrant_workers')
        self.assertEllipsis('...Migrant workers...News...', self.getBody())
        self.get('en/priority_groups/young_people')
        self.assertEllipsis('...Young People - Introduction...Publications...More about...News...Events...', self.getBody())
        self.get('en/priority_groups/gender')
        self.assertEllipsis('...Women and Health at Work...Publications...Practical solutions...News...', self.getBody())
        self.get('en/sector')
        self.assertEllipsis('...Sectors...', self.getBody())
        self.get('en/sector/agriculture')
        self.assertEllipsis('...Agriculture...Publications...', self.getBody())
        self.get('en/sector/construction')
        self.assertEllipsis('...Construction...More about...Publications...News...Events...', self.getBody())
        self.get('/en/sector/education')
        self.assertEllipsis('...Education...More about...Publications...News...', self.getBody())
        self.get('/en/sector/fisheries')
        self.assertEllipsis('...Fisheries...More about...', self.getBody())
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
        




