import unittest
import json 
from app import APP

def login(tester):
    tester.post('api/v1/auth/signup',content_type='application/json',
                                   data =json.dumps( dict(name='moscar@gmail.com',
                                                        password='kmckemekdmekwm')))
    login = tester.post('api/v1/auth/login',content_type='application/json',
                                   data =json.dumps( dict(email='me@gmail.com',
                                                        password='sssd jnjsdnj')))
    return login


class TestProducts(unittest.TestCase):
    def setUp(self):
        self.tester = APP.test_client(self)

def test_get_products(self):
        """test that a products can be got"""
        login_=login(self.tester)
        result = json.loads(login_.data.decode())
        
        self.tester.post('/api/v1/product/', content_type='application/json',
                                   data =json.dumps( dict(name='caps',
                                                        price =23000)),
                         headers =dict(access_token = result['token']))
        self.tester.post('/api/v1/products/', content_type='application/json',
                                   data =json.dumps( dict(name='jeans',
                                                        price=1500)),
                         headers =dict(access_token = result['token']))
        self.tester.post('/api/v1/product/2',
                         headers =dict(access_token = result['token']))
        self.tester.post('/api/v1/products/1',
                         headers =dict(access_token = result['token']))
        response=self.tester.get('/api/v1/product/',
                                 headers =dict(access_token = result['token']))
        self.assertIn(u'jeans', response.data)