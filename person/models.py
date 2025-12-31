from django.db import models


from region.models import City
from user.models import User


class Genre (models.Model):
    GENRE_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    
    name =  models.CharField(max_length=20, choices=GENRE_CHOICES, default='male')
    
    
    def __str__(self):
        return self.name
    
class IdentityDocument (models.Model):
    DOCUMENT_CHOICES = [
        ('dni','DNI'),
        ('passaport','Passaport'),
        ('cpi','CPI')
    ]
    
    name =  models.CharField(max_length=20, choices=DOCUMENT_CHOICES, default='male')
    
    def __str__(self):
        return self.name
    
class MaritalStatus (models.Model):
    MARITAL_STATUS_CHOICE = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated'),
    ]
    
    name =  models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICE, default='male')
    
    def __str__(self):
        return self.name

class Person(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    mail = models.EmailField(max_length=254, null=False, unique=True)
    number_document = models.CharField(max_length=20, null=False, unique=True)
    date_of_birth = models.DateField(null=False)
    phone = models.CharField(max_length=20, null=False, unique=True)
    is_active = models.BooleanField(default=True, null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='person_profiles', null=False)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='people', null=False)
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.PROTECT, related_name='people', null=False)
    identity_document = models.ForeignKey(IdentityDocument, on_delete=models.PROTECT, related_name='people', null=False)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='people', null=False)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.number_document}"