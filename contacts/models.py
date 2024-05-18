from django.db import models

import requests
from bs4 import BeautifulSoup
from .helpers import instadownloader

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_social_media_image(self, platform):
        # could not found an easy way to scrapp images in fb and twitter(X)
        img_url = ""
        if platform == 'facebook' and self.facebook:
            raise NotImplementedError
        elif platform == 'instagram' and self.instagram:
            img_url = instadownloader(profile_name=self.instagram)
        elif platform == 'twitter' and self.twitter:
           raise NotImplementedError

        return img_url

class Phone(models.Model):
    PHONE_CATEGORIES = [
        ('mobile', 'Mobile'),
        ('work', 'Work'),
        ('home', 'Home'),
        ('fax', 'Fax'),
        ('other', 'Other'),
    ]
    contact = models.ForeignKey(Contact, related_name='phones', on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=PHONE_CATEGORIES)
    number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.get_category_display()}: {self.number}"

class Email(models.Model):
    contact = models.ForeignKey(Contact, related_name='emails', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Address(models.Model):
    ADDRESS_CATEGORIES = [
        ('home', 'Home'),
        ('work', 'Work'),
        ('other', 'Other'),
    ]
    contact = models.ForeignKey(Contact, related_name='addresses', on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=ADDRESS_CATEGORIES)
    address = models.TextField()

    def __str__(self):
        return f"{self.get_category_display()}: {self.address}"
