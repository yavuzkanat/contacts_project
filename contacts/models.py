import requests
from bs4 import BeautifulSoup
from django.db import models

from .helpers import instadownloader


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    img_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_social_media_image(self):
        social_media_accounts = self.socialmedia_set.all()
        # walk through the accounts and get the image if exist
        # if not fetch the image and save the url in the model
        for account in social_media_accounts:
            image_url = account.profile_image_url
            if not image_url:
                image_url = account.fetch_profile_image()
            if image_url:
                self.img_url = image_url
                self.save()
                break

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SocialMedia(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
    ]
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    username = models.CharField(max_length=100)
    profile_image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_platform_display()}: {self.username}"

    def fetch_profile_image(self):
        # could not found an easy way (free) to get images in fb and X
        img_url = ""
        if self.platform == 'facebook':
            img_url = "Not yet"
            # raise NotImplementedError
        elif self.platform == 'instagram':
            img_url = instadownloader(profile_name=self.username)
        elif self.platform == 'twitter':
            img_url = "Not yet"
            # raise NotImplementedError
        self.profile_image_url = img_url
        self.save()
        return self.profile_image_url


class Phone(models.Model):
    PHONE_CATEGORIES = [
        ('mobile', 'Mobile'),
        ('work', 'Work'),
        ('home', 'Home'),
        ('fax', 'Fax'),
        ('other', 'Other'),
    ]
    contact = models.ForeignKey(
        Contact, related_name='phones', on_delete=models.CASCADE
    )
    category = models.CharField(max_length=10, choices=PHONE_CATEGORIES)
    number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.get_category_display()}: {self.number}"


class Email(models.Model):
    contact = models.ForeignKey(
        Contact, related_name='emails', on_delete=models.CASCADE
    )
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Address(models.Model):
    ADDRESS_CATEGORIES = [
        ('home', 'Home'),
        ('work', 'Work'),
        ('other', 'Other'),
    ]
    contact = models.ForeignKey(
        Contact, related_name='addresses', on_delete=models.CASCADE
    )
    category = models.CharField(max_length=10, choices=ADDRESS_CATEGORIES)
    address = models.TextField()

    def __str__(self):
        return f"{self.get_category_display()}: {self.address}"
