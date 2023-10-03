from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ContactData(models.Model):
    contact = models.ForeignKey(Contact, related_name="contact_data", on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    DATA_TYPES = (
        ("phone", "Phone"),
        ("email", "Email"),
    )
    data_type = models.CharField(max_length=10, choices=DATA_TYPES, default="phone")

    def __str__(self):
        return self.data
