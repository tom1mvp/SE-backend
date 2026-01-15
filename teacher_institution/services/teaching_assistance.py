from rest_framework.validators import ValidationError
from teacher_institution.repositories.teaching_assistance import TeachingAssistanceRepository

class TeachingAssistanceServices:
    """
    Service layer for Teaching Assistance and Attendance management.
    This class orchestrates business rules and data validation for staff 
    presence records before they are committed to the database.
    """

    @staticmethod
    def get_all_teaching_assistance():
        """
        Retrieves all assistance logs through the repository layer.
        """
        return TeachingAssistanceRepository.get_all_teaching_assistance()
    
    @staticmethod
    def get_teaching_assistance_by_id(teaching_assistance_id):
        """
        Retrieves a specific attendance record based on its unique identifier.
        """
        return TeachingAssistanceRepository.get_teaching_assistance_by_id(teaching_assistance_id)
    
    @staticmethod
    def get_teaching_assistance_by_date(date):
        """
        Fetches attendance records for a specific calendar date.
        Useful for daily institutional compliance checks.
        """
        return TeachingAssistanceRepository.get_teaching_assistance_by_date(date)
    
    @staticmethod
    def get_teaching_assistance_by_name(name):
        """
        Filters attendance records by the teacher's name using 
        related-model lookups.
        """
        return TeachingAssistanceRepository.get_teaching_assistance_by_name(name)
    
    @staticmethod
    def create_teaching_assistance(data, teacher_id):
        """
        Validates the attendance payload and triggers the creation process.
        Ensures that date, reason, and observations are correctly formatted.
        """
        required_fields = [
            'date',
            'reason',
            'observation'
        ]
        
        # Mandatory Field Validation: Guarding against empty or missing data
        for field in required_fields:
            if field not in data or not data[field]:
                # Raising a ValidationError ensures a 400 Bad Request response in the API
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        # Passing validated data to the repository for persistence
        new_teaching_assistance = TeachingAssistanceRepository.create_teaching_assistance(
            date=data['date'],
            reason=data['reason'],
            observation=data['observation'],
            teacher_id=teacher_id
        )
        
        return new_teaching_assistance
    
    @staticmethod
    def update_teaching_assistance(data, teaching_assistance_id, teacher_id):
        """
        Coordinates the update of an existing attendance record.
        Verifies all mandatory fields are present before modifying the record.
        """
        required_fields = [
            'date',
            'reason',
            'observation'
        ]
        
        # Data Integrity Check: Ensuring consistency during the update process
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        # Executing update logic via the repository
        assistance = TeachingAssistanceRepository.update_teaching_assistance(
            teaching_assistance_id=teaching_assistance_id,
            date=data['date'],
            reason=data['reason'],
            observation=data['observation'],
            teacher_id=teacher_id
        )
        
        return assistance