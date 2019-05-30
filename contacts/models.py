from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)


class Friend(models.Model):
    name = models.CharField(max_length=200, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, null=True)
