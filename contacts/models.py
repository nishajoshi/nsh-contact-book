from django.db import models


class Contact(models.Model):
    """Model to store contact."""
    name = models.CharField(max_length=200, null=False)


class Friend(models.Model):
    """Model to store friends and their phone numbers."""
    name = models.CharField(max_length=200, null=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, null=False)
