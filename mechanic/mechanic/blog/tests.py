# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import Post
from django.shortcuts import render_to_response
from django.core.urlresolvers import resolve
from blog.views import post_list


class BlogPageTest(TestCase):
    def test_blog_page_resolves(self):
        blog_page = resolve('/blog/')
        self.assertEqual(blog_page.func, post_list)



class PostTests(TestCase):
   
    def test_str(self):
        test_title = Post(title='A new car blog post')
        self.assertEqual(str(test_title),
                          'Another title')



