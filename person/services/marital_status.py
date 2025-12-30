from person.repositories.maritial_status import MaritalStatusRepository


class MaritalStatusServices:
    """
    Marital Status Management Service

    Manages the business logic associated with civil status classifications.
    This service ensures that personal data for parents, guardians, and staff
    is handled consistently, supporting administrative accuracy and family 
    relationship mapping.

    Business Logic Handled:
    - Data Provisioning: Supplies validated marital status options for user interfaces.
    - Integrity Checks: Facilitates the retrieval of specific records for profile updates.
    """
    
    @staticmethod
    def get_all_marital_status():
        # Retrieves the complete list of marital status categories for the system.
        return MaritalStatusRepository.get_all_marital_status()
    
    @staticmethod
    def get_marital_status_by_id(marital_status_id):
        # Business logic to obtain a specific marital status record by its unique ID.
        return MaritalStatusRepository.get_marital_status_by_id(marital_status_id)
    
    @staticmethod
    def get_marital_status_by_name(marital_status_name):
        # Filters marital status options by name to support search and auto-complete features.
        return MaritalStatusRepository.get_marital_status_by_name(marital_status_name)