import re
import unittest

import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
    
    def test_get(self):
        g = self.app.get('/')
        assert g.status_code == 200
        assert re.match(r'^Greetings from server [\w.-]+$', g.data, re.I)


if __name__ == '__main__':
    unittest.main()
