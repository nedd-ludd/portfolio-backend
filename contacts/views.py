from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .amazon_ses import Email

from .models import Contact
from .serializers import ContactSerializer

class ContactListView(APIView):

    def get(self, _request):
        contacts = Contact.objects.all()
        serialized_contacts = ContactSerializer(contacts, many=True)
        return Response(serialized_contacts.data, status=status.HTTP_200_OK )
    
    def post(self, request):
        email = Email(
         name = request.data["name"],
         phone = request.data["phone"],
         email = request.data["email"],
         subject = request.data["subject"],
         message = request.data["message"]
        )
        email.send()
        return Response(request.data, status=status.HTTP_201_CREATED)