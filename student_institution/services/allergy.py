from rest_framework.validators import ValidationError


from student_institution.repositories.allergy import AllergyRepository


class AllergyServices:
    """
    Service layer to manage business logic and validation for AllergyKind.
    Acts as an intermediary between the API views and the data repository.
    """

    @staticmethod
    def get_all_allergy():
        """Fetches all allergy types through the repository."""
        return AllergyRepository.get_all_allergy()
    
    @staticmethod
    def get_allergy_by_id(allergy_id):
        """Retrieves a specific allergy by its ID."""
        return AllergyRepository.get_allergy_by_id(allergy_id)
    
    @staticmethod
    def get_allergy_by_name(allergy_name):
        """Retrieves an allergy record by performing a name-based search."""
        return AllergyRepository.get_allergy_by_name(allergy_name)
    
    @staticmethod
    def create_allergy(
        data
    ):
        """
        Validates that the 'name' field is present in the input data
        before requesting the repository to create a new record.
        """
        required_fields = ['name']
        
        for field in required_fields:
            if field not in data:
                # Raises a 400 Bad Request error if validation fails
                raise ValidationError({field: f'El campo {field} es obligatorio'})
        
        new_allergy = AllergyRepository.create_allergy(
            name=data['name']
        )
        
        return new_allergy
    
    @staticmethod
    def update_allergy(
        data,
        allergy_id
    ):
        """
        Coordinates the update process for an existing allergy record
        using the provided data and ID.
        """
        allergy = AllergyRepository.update_allergy(
            allergy_id=allergy_id,
            name=data['name']
        )
        
        return allergy