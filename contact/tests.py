import random
import string
from django.test import TestCase
from contact.models import Contact, Phone

# Create your tests here.

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def random_num(y):
    return ''.join(str(random.randint(0,9)) for x in range(y))


class UnitTestCase(TestCase):

    name = random_char(random.randint(0, 9))


    def setUp(self):

        contact = Contact.objects.create(name = self.name, email= self.name+"@gmail.com")
        phone = Phone.objects.create(number = random_num(10), contact = contact)

    def getPhonefromContact(self):

        phone = Phone.objects.filter(contact__name=self.name)[0]
        self.assertEqual(phone.contact.name, self.name)





