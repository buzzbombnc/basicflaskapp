import re
import random
import time
import unittest

import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        # Do some fake setup that takes 15-30 seconds.
        time.sleep(random.randint(0, 15) + 15)
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
    
    def test_get(self):
        g = self.app.get('/')
        assert g.status_code == 200
        assert re.match(r'^[0-9.]+    [\w.-]+$', g.data, re.I)


if __name__ == '__main__':
    unittest.main()
