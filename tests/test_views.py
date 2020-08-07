from django.test import TestCase, Client
from django.urls import reverse
from generator.views import home, password, about
import datetime


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_GET(self):

        response = self.client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gen/home.html')
    

    
    def test_about_GET(self):
        response = self.client.get(reverse('about'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gen/about.html')
    
    def test_password_GET(self):
        response = self.client.get(reverse('password'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gen/pass.html')
    
    def test_password_check_length(self):
        
        response = self.client.get('/password/?length=7')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.context['password']), 7)
    
    def test_password_check_uppercase(self):
        
        response = self.client.get('/password/?uppercase=on')

        t = any(x.isupper() for x in response.context['password'])

        self.assertEquals(response.status_code, 200)
        self.assertEquals(t, True)
    
    def test_password_check_special_characters(self):
        
        response = self.client.get('/password/?special=on')

        t = any( not x.isalnum() for x in response.context['password'])

        self.assertEquals(response.status_code, 200)
        self.assertEquals(t, True)
    
    def test_password_check_numbers(self):
        
        response = self.client.get('/password/?numbers=on&length=20')

        t = any( x.isdigit() for x in response.context['password'])

        self.assertEquals(response.status_code, 200)
        self.assertEquals(t, True)
    
    def test_about_year(self):
        response = self.client.get('/about/')

        self.assertEquals(response.context['date'], datetime.datetime.now().year)
        self.assertEquals(response.status_code, 200)

    
