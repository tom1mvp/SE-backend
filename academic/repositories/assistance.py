from academic.models import Assistance, ModalityAssistance
from student_institution.models import Student

"""
    Academic Assistance Repository
    
    This module encapsulates all database operations for student attendance records.
    It provides a clean API for the service layer to interact with Assistance data,
    ensuring proper handling of relationships with Students and Modalities.
"""

class AssistanceRepository:
    # Retrieves the complete collection of attendance records from the database.
    @staticmethod
    def get_all_assistance():
        return Assistance.objects.all()
    
    # Returns the most recent or specific attendance record for a given student ID.
    @staticmethod
    def get_assistance_by_student(student_id):
        return Assistance.objects.filter(student__id=student_id).first()
    
    # Filters attendance records based on a specific calendar date.
    @staticmethod
    def get_assistance_by_date(date):
        return Assistance.objects.filter(date=date)
    
    # Handles the complex logic of creating a new attendance entry with foreign key validation.
    @staticmethod
    def create_assistance(
      date,
      observation,
      modality_id,
      student_id,
      is_absence
    ):
        # Verification of the existence of the selected modality before persistence.
        modality = ModalityAssistance.objects.filter(id=modality_id).first()
        
        if not modality:
            raise ValueError('error', 'Modality not found')
        
        # Ensures the record is linked to a valid student within the institution.
        student = Student.objects.filter(id=student_id).first()
        
        if not student:
            raise ValueError('error', 'Student not found')
        
        # Persists the validated attendance record into the database.
        new_assistance = Assistance.objects.create(
            date=date,
            observation=observation,
            modality=modality,
            student=student,
            is_absence=is_absence
        )
        
        return new_assistance
    
    # Manages the update transaction for existing attendance records.
    @staticmethod
    def update_assistance(
        assistance_id,
        date,
        observation,
        modality_id,
        student_id,
        is_absence
    ):
        # Locates the target record for modification.
        assistance = Assistance.objects.filter(id=assistance_id).first()
        
        if not assistance:
            raise ValueError('error', 'Assistance not found')
        
        # Re-validates the modality relationship for the update.
        modality = ModalityAssistance.objects.filter(id=modality_id).first()
        
        if not modality:
            raise ValueError('error', 'Modality not found')
        
        # Re-validates the student relationship for the update.
        student = Student.objects.filter(id=student_id).first()
        
        if not student:
            raise ValueError('error', 'Student not found')
        
        # Atomic update of attributes.
        assistance.date=date
        assistance.observation=observation
        assistance.modality=modality
        assistance.student=student
        assistance.is_absence=is_absence
        
        # Commits the changes to the database.
        assistance.save()
        
        return assistance

