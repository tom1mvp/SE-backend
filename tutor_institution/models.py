from django.db import models

from person.models import Person

class Tutor(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='tutors', null=False)

    def __str__(self):
        return f'Name: {self.person.first_name} || Last name: {self.person.last_name} ({self.relationship})'