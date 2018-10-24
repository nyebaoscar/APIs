import unittest
import json 

class TestUserApi(unittest.TestCase):
    def setUp(self):

        def test_successful_signup(self):

                
             response = self.tester.post('api/v1/auth/signup',content_type='application/json',data=json.dumps(dict(email='oscar@gmail.com',
             password='desssssssssssssssss')))
             self.assertIn("successfull signed in",response.data)
             self.assertEqual(response.status_code,201)
    
    def test_wrong_credentials_signup(self):
        '''unique user can be added'''
        self.tester.post('api/v1/auth/signup',content_type='application/json',data=json.dumps(dict(email='dams@gmail.com',
        password='snbjgnbnbjnbj')))
        response = self.tester.post('api/v1/auth/signup/',content_type='application/json',data=json.dumps(dict(email='dams@gmail.com',
        password='snbjgnbnbjnbj')))
        self.assertIn("user already exists",response.data)
        self.assertEqual(response.status_code,401)

if __name__== "__main__":
    unittest.main