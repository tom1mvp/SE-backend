from rest_framework.validators import ValidationError


from academic.repositories.modality_assistance import ModalityAssistanceRepository


"""
    Academic Modality Assistance Service Layer
    
    This module manages the business logic for defining different attendance modalities 
    (e.g., Morning, Afternoon, Virtual). It acts as a configuration layer to ensure 
    consistency in how assistance is categorized throughout the institution.
"""

class ModalityAssistanceServices:
    @staticmethod
    def get_all_modality_assitance():
        return ModalityAssistanceRepository.get_all_modality_assistance()
    
    # Coordinates the creation of a new attendance modality after data validation.
    @staticmethod
    def create_modality_assitance(data):
        # List of essential attributes required to define a modality.
        required_fields = ['name']
        
        # Data Integrity Check: Verify that all required fields have been provided in the payload.
        for field in required_fields:
            if field not in data:
                # Standardized error message for institutional consistency.
                raise ValidationError({field: f'The field {field} is mandatory.'})
        
        # Triggers the repository logic to persist the new modality in the database.
        new_modality_assistance = ModalityAssistanceRepository.create_modality_assistance(
            name=data['name']
        )
        
        return new_modality_assistance