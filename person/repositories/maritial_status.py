from person.models import MaritalStatus


class MaritalStatusRepository:
    """
    Marital Status Management Repository

    Handles the persistence logic for civil status classifications. 
    This data is essential for administrative records of parents, legal guardians, 
    and staff members, ensuring accurate family and emergency contact profiles.

    Methods:
    - GET:
        * List all registered marital status options.
        * Retrieve a specific status by ID (Primary Key).
        * Search for status types by name (e.g., Single, Married, Divorced).
    """

    @staticmethod
    def get_all_marital_status():
        # Retrieve the full list of marital status categories from the database.
        return MaritalStatus.objects.all()
    
    @staticmethod
    def get_marital_status_by_id(marital_status_id):
        # Fetch a specific status record using its unique identifier.
        return MaritalStatus.objects.filter(id=marital_status_id).first()
    
    @staticmethod
    def get_marital_status_by_name(marital_status_name):
        # Find marital status records based on name matches for form population.
        # Returns a QuerySet for broad search capabilities.
        return MaritalStatus.objects.filter(name__icontains=marital_status_name).first()