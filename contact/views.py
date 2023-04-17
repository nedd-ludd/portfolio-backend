
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Contact
from .serializers import ContactSerializer


class ContactListView(APIView):
  #TODO: DELETE GET WHEN DONE - one way only 

    def get(self, _request):
        contacts = Contact.objects.all()  # get everything from the shows table in the db
        # run everything through the serializer
        serialized_contacts = ContactSerializer(contacts, many=True)
        # return the response and a status
        return Response(serialized_contacts.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        return Response(request.data, status=status.HTTP_200_OK)
        

