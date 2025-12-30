from django.db import models


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