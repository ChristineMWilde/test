# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.shortcuts import render_to_response
from django.core.urlresolvers import resolve
from views import forum
from .models import Subject
from accounts.models import User
from .forms import ThreadForm
from django import forms
from django.conf import settings



class ForumPageTest(TestCase):
    def test_forum_page_resolves(self):
        forum_page = resolve('/forum/')
        self.assertEqual(forum_page.func, forum)



class SubjectPageTest(TestCase):

    fixtures = ['subjects', 'user']

    def test_check_content_is_correct(self):
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum/forum.html")
        subject_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects': Subject.objects.all()}).content
        self.assertEquals(subject_page.content, subject_page_template_output)



class CustomUserTest(TestCase):
    def test_thread_form(self):
        form = ThreadForm({
            'name': 'testname'
        })
 
        self.assertTrue(form.is_valid())


    def test_thread_form_no_name_for_thread(self):
        form = ThreadForm({
            'name': '""'
        })
 
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Enter a name",
                                 form.full_clean())