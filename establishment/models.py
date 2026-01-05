from django.db import models


from region.models import City
from academic.models import ElectiveCycle


class Address(models.Model):
    street = models.CharField(max_length=150, null=False)
    number = models.CharField(max_length=10, null=False)
    comment = models.TextField(max_length=255, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='addresses', null=False)
    
    def __str__(self):
        return f'Street: {self.street} || Number: {self.number} || City: {self.city.name}'
    
class InstitutionCategory(models.Model):
    name = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.name
    
class Institution(models.Model):
    name = models.CharField(max_length=150, null=False)
    opening_hour = models.TimeField(null=False)
    closing_hour = models.TimeField(null=False)
    logo_url = models.ImageField(upload_to='institution/logos/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(InstitutionCategory, on_delete=models.PROTECT, related_name='institutions', null=False)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='institution', null=False)
    elective_cycle = models.ForeignKey(ElectiveCycle, on_delete=models.PROTECT, related_name='institutions', null=False)
    
    def __str__(self):
        return f'Name: {self.name} || Open: {self.opening_hour} || Close: {self.closing_hour}'
    
class HistoryInstitution(models.Model):
    biography = models.TextField(null=False)
    foundation_date = models.DateField(null=False)
    multimedia_url = models.ImageField(upload_to='institution/history/', null=True, blank=True)
    founder = models.CharField(max_length=150, null=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='history', null=False)
    
    def __str__(self):
        return f'Foundation date: {self.foundation_date} || Founder: {self.founder} || Institution: {self.institution.name}'