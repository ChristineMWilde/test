# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.shortcuts import render_to_response
from accounts.models import User
from django.core.urlresolvers import resolve
from home.views import get_index


class HomeURLTest(TestCase):
	def test_home_page_status_code(self):
		home_page = self.client.get('/')
		self.assertEqual(home_page.status_code, 200)


	def test_check_contect_works(self):
		home_page = self.client.get('/')
		self.assertTemplateUsed(home_page, "index.html")
		home_page_template_output = render_to_response("index.html").content
		self.assertEqual(home_page.content, home_page_template_output) 

class HomePageTest(TestCase):
 
    def setUp(self):
        super(HomePageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('logmein')
        self.user.save()
 
    def test_login(self):
        login = self.client.login(username='testuser', password='logmein')
        self.assertTrue(login)
 
    def test_home_page_index_view_usage(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)
 
    def test_home_page_index_template_usage(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
 
    def test_home_page_logged_in_content(self):
        self.client.login(username='testuser', password='logmein')
        home_page = self.client.get('/')
 
        home_page_template_output = render_to_response(
            "index.html", {'user': self.user}).content
        self.assertEquals(home_page.content, home_page_template_output)