from django.test import SimpleTestCase
from django.urls import reverse, resolve
from generator.views import home, password, about 


class TestUrls(SimpleTestCase):
    def test_url_home(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
    
    def test_url_password(self):
        url = reverse('password')
        self.assertEquals(resolve(url).func, password)
    
    def test_url_about(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

