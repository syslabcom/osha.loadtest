from webunit.utility import Upload
import funkload.Lipsum
import funkload.utils
import os
import tempfile
import osha.loadtest.base


LIPSUM = funkload.Lipsum.Lipsum()

class medium(osha.loadtest.base.TestCase):
    is_epp = False
    group = 'mediumusagegroup'


    def setUp(self):
        pass
        
    def setUpBench(self):
        pass

    def tearDown(self):
        pass

    def tearDownBench(self):
        pass

    def test_medium(self):
        """ Implements the following medium usage steps
    	* Login via the main home page URL
    	* Logoff
    	"""
        self.get('/en/practical-solutions')
        self.assertEllipsis('...Practical Solutions...Online interactive Risk Assessment tool...', self.getBody())
        self.get('en/practical-solutions/useful-links')
        self.assertEllipsis('...Useful Links...Online interactive Risk Assessment tool...', self.getBody())
        self.get('en/practical-solutions/risk-assessment-tools')
        self.assertEllipsis('...Risk Assessment Tools...', self.getBody())
        self.get('en/practical-solutions/case-studies')
        self.assertEllipsis('...Case Studies...', self.getBody())
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
        self.get('/en/esener-enterprise-survey')
        self.assertEllipsis('...Enterprise survey on new and emerging risks...', self.getBody())
        # indicator.gif fehlt (von einem nicht mehr verwendeten prokukt, lt. Wolfgang)
        # self.get('/sub/esener/en/front-page/182/014')
        # self.assertEllipsis('...ESENER survey results 2009...', self.getBody())
        self.get('/sub/esener/en/front-page/download.xls?question=182&country=014&group_by=')
        self.get('/en/practical-solutions/risk-assessment-tools/index_html/practical-solution?SearchableText=risk&is_search_expanded=&getRemoteLanguage=en&keywords%3Alist=&nace2=&multilingual_thesaurus2=&submit=Search')
        self.assertEllipsis('...Risk Assessment Tools...Search results...', self.getBody())
        # https://projects.syslab.com/issues/5811
        # self.get('/en/publications/literature_reviews/risk-perception-and-risk-communication-with-regard-to-nanomaterials-in-the-workplace/view')
        # self.assertEllipsis('...Risk perception...', self.getBody())
        self.get('/en/publications/literature_reviews/risk-perception-and-risk-communication-with-regard-to-nanomaterials-in-the-workplace')

