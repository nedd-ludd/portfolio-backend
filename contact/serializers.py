from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact  # the model it should use
        fields = '__all__'  # which fields to serialize