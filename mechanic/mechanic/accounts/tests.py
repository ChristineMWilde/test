# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import User
from .forms import UserRegistrationForm
from django import forms
from django.conf import settings
 
 
class CustomUserTest(TestCase):
 
    def test_manager_create(self):
        user = User.objects._create_user(None, "me@test.com",
                                         "password",
                                         False, False)
        self.assertIsNotNone(user)
 
        with self.assertRaises(ValueError):
            user = User.objects._create_user(None, None, "password",
                                             False, False)


 
    def test_registration_form(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'logmein1',
            'password2': 'logmein1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 5555555555554444,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2021
        })
 
        self.assertTrue(form.is_valid())


    def test_registration_form_with_missing_email(self):
        form = UserRegistrationForm({
            'password1': 'logmein1',
            'password2': 'logmein1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 5555555555554444,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2021
        })
 
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Email is missing, please enter",
                                 form.full_clean())
  
    
    
    def test_registration_form_password_mismatch(self):
        form = UserRegistrationForm({
        	'email': 'test@test.com',
            'password1': 'logmein1',
            'password2': 'test3',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 5555555555554444,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2021
        })
 
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())




    def test_registration_form_missing_password(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 5555555555554444,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2021
        })
        
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Missing password.",
                                 form.full_clean())


    def test_registration_form_invalid_card(self):
        form = UserRegistrationForm({
        	'password1': 'logmein1',
            'password2': 'logmein1',
            'email': 'test@test.com',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 555555,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2021
        })
        
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Invalid Card.",
                                 form.full_clean())
