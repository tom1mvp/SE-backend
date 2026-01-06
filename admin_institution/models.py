from django.db import models
from establishment.models import Institution
from person.models import Person

class Admin(models.Model):
    operating_range = models.CharField(max_length=50, null=False)
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT, null=False)
    person = models.OneToOneField(Person, on_delete=models.PROTECT, null=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Person name: {self.person.first_name} || User: {self.person.user.username} || Institution: {self.institution.name}'
    
