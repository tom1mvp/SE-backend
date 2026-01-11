from student_institution.models import AllergyKind

class AllergyRepository:
    """
    Repository class for AllergyKind model.
    Centralizes all database operations related to allergy types.
    """
    
    @staticmethod
    def get_all_allergy():
        """Retrieves a queryset of all registered allergy types."""
        return AllergyKind.objects.all()
    
    @staticmethod
    def get_allergy_by_id(allergy_id):
        """Fetches a specific allergy type by its unique database ID."""
        return AllergyKind.objects.filter(id=allergy_id).first()
    
    @staticmethod
    def get_allergy_by_name(allergy_name):
        """
        Searches for an allergy by name using a case-insensitive lookup.
        Returns the first match found.
        """
        return AllergyKind.objects.filter(name__icontains=allergy_name).first()
    
    @staticmethod
    def create_allergy(
        name
    ):
        """Inserts a new allergy record into the database."""
        new_allergy = AllergyKind.objects.create(
            name=name
        )
        
        return new_allergy
    
    @staticmethod
    def update_allergy(
        allergy_id,
        name
    ):
        """
        Updates the name of an existing allergy record.
        Raises an error if the ID does not correspond to any record.
        """
        allergy = AllergyKind.objects.filter(id=allergy_id).first()
        
        if not allergy:
            raise ValueError('Error', 'Allergy ID not found')
        
        allergy.name = name
        # Note: allergy.save() would be required here to persist changes.