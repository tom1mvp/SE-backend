from academic.models import ModalityAssistance


"""
    Academic Modality Assistance Repository
    
    This module manages the persistence of attendance modalities.
    It provides a standardized interface for creating and storing
    different methods of student attendance, ensuring consistency
    across the academic tracking system.
"""

class ModalityAssistanceRepository:
    @staticmethod
    def get_all_modality_assistance():
        return ModalityAssistance.objects.all()
        
    # Persists a new attendance modality (e.g., "Morning", "Virtual") in the database.
    @staticmethod
    def create_modality_assistance(
        name
    ):
        # Creates a new record using the provided modality name.
        new_modality_assistance = ModalityAssistance.objects.create(
            name=name
        )
        
        return new_modality_assistance