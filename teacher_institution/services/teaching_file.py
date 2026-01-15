from rest_framework.validators import ValidationError
from teacher_institution.repositories.teaching_file import TeachingFileRepository

class TeachingFileServices:
    """
    Service layer for TeachingFile management.
    This class handles business logic, data validation, and coordinates 
    between the API views and the Repository layer.
    """

    @staticmethod
    def get_all_teaching_file():
        """
        Retrieves all professional records through the repository.
        """
        return TeachingFileRepository.get_all_teaching_file()
    
    @staticmethod
    def get_teaching_file_by_id(teaching_file_id):
        """
        Retrieves a specific file record by its unique ID.
        """
        return TeachingFileRepository.get_teaching_file_by_id(teaching_file_id)
    
    @staticmethod
    def get_teaching_file_by_number(number):
        """
        Retrieves a professional record using the file number identifier.
        """
        return TeachingFileRepository.get_teaching_file_by_number(number)
    
    @staticmethod
    def create_teaching_file(data):
        """
        Validates incoming data and creates a new TeachingFile.
        Ensures all mandatory administrative fields are present before persistence.
        """
        required_fields = [
            'number',
            'license_number',
            'date_admission'
        ]
        
        # Data Integrity Check: Verify all required fields are provided in the payload
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        # Delegating object creation to the Repository layer
        new_teaching_file = TeachingFileRepository.create_teaching_file(
            number=data['number'],
            license_number=data['license_number'],
            date_admission=data['date_admission']
        )
        
        return new_teaching_file
    
    @staticmethod
    def update_teaching_file(data, teaching_file_id):
        """
        Updates an existing professional record after validating the new data.
        """
        required_fields = [
            'number',
            'license_number',
            'date_admission'
        ]
        
        # Data Integrity Check: Ensuring consistency during the update process
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        # Committing updates through the repository
        teaching_file = TeachingFileRepository.update_teaching_file(
            teaching_file_id=teaching_file_id,
            number=data['number'],
            license_number=data['license_number'],
            date_admission=data['date_admission']
        )
        
        return teaching_file