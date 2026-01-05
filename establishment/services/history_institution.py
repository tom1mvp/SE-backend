"""
History Institution Management Service

This service manages the biographical and foundational records of educational 
entities. It ensures that historical data, such as founding dates and 
biographies, are validated before being linked to the primary institutional 
record.

Business Logic:
- Record Integrity: Validates presence of biography, founder, and foundation date.
- Archival Management: Facilitates access to historical data for administrative 
  and public display purposes.
- Context Linking: Coordinates the relationship between history records and 
  their parent institutions.
"""

from rest_framework.validators import ValidationError
from establishment.repositories.history_institucion import HistoryInstitutionRepository


class HistoryInstitutionServices:
    @staticmethod
    def get_all_history():
        # Proxies the request to retrieve the full archive of institutional histories.
        return HistoryInstitutionRepository.get_all_history_institution()
    
    @staticmethod
    def get_history_institutional_by_id(history_institutional_id):
        # Fetches a specific historical entry by its unique identifier.
        return HistoryInstitutionRepository.get_history_institution_by_id(history_institutional_id)
    
    @staticmethod
    def get_history_institution_by_institution(institution_id):
        # Retrieves historical records associated with a specific institution.
        return HistoryInstitutionRepository.get_history_institution_by_institution(institution_id)
    
    @staticmethod
    def create_history_institution(
        data,
        institution_id
    ):
        # Defines the mandatory fields for the institutional legacy records.
        required_fields = [
            'biography',
            'foundation_date',
            'multimedia_url',
            'founder'
        ]
        
        # Validates that all required historical data is provided in the request.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
        
        # Triggers the creation of the history record via the repository.
        new_history_institutional = HistoryInstitutionRepository.create_history_institution(
            biography=data['biography'],
            foundation_date=data['foundation_date'],
            multimedia_url=data['multimedia_url'],
            founder=data['founder'],
            institution_id=institution_id
        )
        
        return new_history_institutional
    
    @staticmethod
    def update_history_institution(
        data,
        history_institution_id,
        institution_id
    ):
        
        # Mandatory attributes check for maintaining consistent historical logs.
        required_fields = [
            'biography',
            'foundation_date',
            'multimedia_url',
            'founder'
        ]
        
        # Ensures the update payload contains all necessary narrative details.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})

        # Synchronizes the updated historical data with the existing database record.
        history_institutional = HistoryInstitutionRepository.update_history_institution(
            history_institution_id=history_institution_id,
            biography=data['biography'],
            foundation_date=data['foundation_date'],
            multimedia_url=data['multimedia_url'],
            founder=data['founder'],
            institution_id=institution_id
        )
        
        return history_institutional