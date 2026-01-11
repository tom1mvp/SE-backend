from django.db import models


from establishment.models import Institution
from person.models import Person
from academic.models import ElectiveCycle, Subject
        
class AllergyKind(models.Model):
    name = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.name

class StudentFile(models.Model):
    number = models.CharField(max_length=10, null=False, unique=True)
    date_admission = models.DateField(null=False)
    sanguine_group = models.CharField(max_length=5, null=False)
    is_allergic = models.BooleanField(default=False)
    photo_url = models.ImageField(upload_to='institution/student/photo/', null=True, blank=True)
    social_work_name = models.CharField(max_length=50, null=False)
    social_work_number = models.CharField(max_length=5, null=False, unique=True)
    emergency_contact_name = models.CharField(max_length=50, null=False)
    emergency_contact_phone = models.CharField(max_length=12, null=False)
    status = models.BooleanField(default=True)
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT, related_name='student_file', null=False)
    allergy = models.ForeignKey(AllergyKind, on_delete=models.PROTECT, related_name='student_file', null=False)
    
    def __str__(self):
        return f'File: {self.number}'
    
class Student(models.Model):
    person = models.OneToOneField(Person, on_delete=models.PROTECT, related_name='student', null=False)
    student_file = models.ForeignKey(StudentFile, on_delete=models.PROTECT, related_name='student', null=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"First name: {self.person.first_name}|| Last name: {self.person.last_name} || File: {self.student_file.number}"
    
    
class SubjectEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='subject_enrollment', null=False)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name='subject_enrollment', null=False)
    elective_cycle = models.ForeignKey(ElectiveCycle, on_delete=models.PROTECT, related_name='subject_enrollment', null=False)
    
    
    def __str__(self):
        return f'Student: {self.student.person.first_name} {self.student.person.last_name} || Subject name: {self.subject.name}'