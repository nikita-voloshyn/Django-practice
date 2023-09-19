from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)


class ContactData(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=20)
    data_value = models.CharField(max_length=100)
