from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    
    def __str__(self):
        return f"{self.name}"
    
