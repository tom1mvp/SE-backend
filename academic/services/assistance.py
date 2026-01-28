from rest_framework.validators import ValidationError


from academic.repositories.assistance import AssistanceRepository


"""
    Academic Assistance Service Layer
    
    This module coordinates the business logic for student attendance tracking. 
    It acts as a validation bridge between the API views and the repository, 
    ensuring that daily records and absence logs maintain institutional integrity.
"""

class AssistanceServices:
    # Fetches the complete history of student attendance records.
    @staticmethod
    def get_all_assistance():
        return AssistanceRepository.get_all_assistance()
    
    # Retrieves all attendance logs associated with a specific student.
    @staticmethod
    def get_assistance_by_student(student_id):
        return AssistanceRepository.get_assistance_by_student(student_id)
    
    # Filters the assistance database by a specific calendar date.
    @staticmethod
    def get_assistance_by_date(date):
        return AssistanceRepository.get_assistance_by_date(date)
    
    # Orchestrates the creation of a new attendance record with strict field validation.
    @staticmethod
    def create_assistance(data, modality_id, student_id):
        # Definition of mandatory attributes for a valid attendance entry.
        required_fields = [
            'date',
            'observation',
            'is_absence',
        ]
        
        # Data Integrity Validation: Ensures all required keys are present in the payload.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        # Persists the new record through the repository layer.
        new_assistance = AssistanceRepository.create_assistance(
            date=data['date'],
            observation=data['observation'],
            modality_id=modality_id,
            student_id=student_id,
            is_absence=data['is_absence']
        )
        
        return new_assistance
    
    # Manages the update lifecycle for existing attendance logs.
    @staticmethod
    def update_assistance(data, assistance_id, modality_id, student_id):
        required_fields = [
            'date',
            'observation',
            'is_absence',
        ]
        
        # Validates data consistency before executing the update transaction.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'The field {field} is mandatory.'})
        
        # Triggers the repository update with validated institutional data.
        assistance = AssistanceRepository.update_assistance(
            assistance_id=assistance_id,
            date=data['date'],
            observation=data['observation'],
            modality_id=modality_id,
            student_id=student_id,
            is_absence=data['is_absence']
        )
        
        return assistance