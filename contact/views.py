from rest_framework.permissions import IsAuthenticated
from contact.models import Contact, Phone
from rest_framework import viewsets
from contact.serializers import ContactSerializer, PhoneSerializer
from rest_framework import filters

# Create your views here.

class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')



class PhoneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows photos to be viewed or edited.
    """

    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)


