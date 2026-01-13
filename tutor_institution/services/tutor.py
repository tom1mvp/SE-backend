from rest_framework.validators import ValidationError

from tutor_institution.repository.tutor import TutorRepository


class TutorServices:
    """
    Service layer class that acts as an intermediary between the API views and 
    the data access layer (Repository). This class handles business logic, 
    data validation, and ensures that the repository receives clean data.
    """

    @staticmethod
    def get_all_tutor():
        """
        Coordinates the retrieval of all tutor records.
        It bypasses business logic to directly fetch the full collection from the repository.
        """
        return TutorRepository.get_all_tutor()
    
    @staticmethod
    def get_tutor_by_id(tutor_id):
        """
        Business logic to find a specific tutor by its primary key.
        Ensures that the requested ID is processed through the repository's lookup logic.
        """
        return TutorRepository.get_tutor_by_id(tutor_id)
    
    @staticmethod
    def get_tutor_by_name(name): 
        """
        Service-level method to filter tutors based on their personal first name.
        Facilitates searching across related models via the repository.
        """
        return TutorRepository.get_tutor_by_name(name)
    
    @staticmethod
    def get_tutor_by_relationship(relationship):
        """
        Handles the request to filter tutors by their family or legal link to a student.
        Useful for organizational reporting or emergency contact management.
        """
        return TutorRepository.get_tutor_by_relationship(relationship)
    
    @staticmethod
    def create_tutor(
        data,
        person_id
    ):
        """
        Validates incoming payload data and manages the creation process of a new Tutor.
        This method ensures that all business requirements (like mandatory fields) 
        are met before requesting the repository to persist the data.
        """
        # Define the list of attributes that must be present in the request
        required_fields = ['relationship']
        
        # Verify that all required fields in the form have been filled in.
        # This loop acts as a primary guard against incomplete data submissions.
        for field in required_fields:
            if field not in data:
                # Raising a DRF ValidationError ensures the API returns a 400 Bad Request
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        # Once validated, the data is passed to the repository for database insertion
        new_tutor = TutorRepository.create_tutor(
            person_id=person_id,
            relationship=data['relationship']
        )
        
        return new_tutor