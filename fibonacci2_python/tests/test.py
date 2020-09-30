import unittest
from flask import Flask
from fibonacci2 import app


class TestFib(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def tearDown(self):
        pass 

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 404) 

    def test_fib_data_2(self):
        result = self.app.get('/fib/2') 

        # assert the response data
        self.assertIn('"result": "[[2]]"', str(result.data))
        

    def test_fib_data_3(self):
        result = self.app.get('/fib/3') 

        # assert the response data
        self.assertIn('"result": "[[3]]"', str(result.data))
    
    def test_fib_data_11(self):
        result = self.app.get('/fib/11') 

        # assert the response data
        self.assertIn('[2, 2, 2, 2, 3]', str(result.data))
        self.assertIn('[2, 2, 2, 5]', str(result.data))
        self.assertIn('[2, 3, 3, 3]', str(result.data))
        self.assertIn('[3, 3, 5]', str(result.data))
        self.assertIn('[3, 8]', str(result.data))
        
    def test_health_data_(self):
        result = self.app.get('/health') 

        # assert the response data
        self.assertIn('"hostname":', str(result.data))
        
        
        
if __name__ == "__main__":
    unittest.main()
