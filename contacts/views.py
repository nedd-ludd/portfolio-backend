from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Contact
from .serializers import ContactSerializer

class ContactListView(APIView):

    def get(self, _request):
        contacts = Contact.objects.all()
        serialized_contacts = ContactSerializer(contacts, many=True)
        return Response(serialized_contacts.data, status=status.HTTP_200_OK )