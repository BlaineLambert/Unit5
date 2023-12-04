from django.db import models

# Create your models here.
class Contact_model(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
def create(name, number, email):
    person = Contact_model(name = name, number = number, email = email)
    person.save()
    print(person)
    return person
