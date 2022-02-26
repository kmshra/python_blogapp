from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    course = models.CharField(max_length=50)
    remarks= models.TextField()

    def __str__(self):
        return 'Enquiry from ' + self.name

   
    

