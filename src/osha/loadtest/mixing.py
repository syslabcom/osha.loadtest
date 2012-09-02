import random
from light import light, light_epp
from medium import medium, medium_epp
from heavy import heavy, heavy_epp
from admin import admin_epp

class mixing(light, medium, heavy):
    
    def setUp(self):
        pass
    
    def setUpBench(self):
        pass
        
    def test_mixing(self):
        # run this with 9 cycles for debugging only, we don't have epp locally, so no admin test
        
        rnd = random.randint(1, 100)
        if rnd < 40:
            # 4 light usage users
            return self.test_light()
        elif rnd < 60:
            # 2 medium users
            return self.test_medium()
        else:
            # 4 heavy users
            return self.test_heavy()
        
class mixing_epp(light_epp, medium_epp, heavy_epp, admin_epp):
    
    
    def setUp(self):
        pass

    def setUpBench(self):
        pass
    
    def test_mixing(self):
        # run this with 100 cycles
        rnd = random.randint(1, 100)
        if rnd < 40:
            # 40 light usage users
            return self.test_light()
        elif rnd < 60:
            # 20 medium users
            return self.test_medium()
        elif rnd < 90:
            # 30 heavy users
            return self.test_heavy()
        else:
            # 10 admin users
            return self.test_admin()
