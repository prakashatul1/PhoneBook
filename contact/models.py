from django.db import models

# Create your models here.

from django.db import models


# Create your models here.
class Contact(models.Model):

    email = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50, blank = True, null=True)


class Phone(models.Model):

    number = models.IntegerField(blank = True, null=True)
    contact = models.ForeignKey(Contact, blank =True,null=True, on_delete=models.CASCADE)
