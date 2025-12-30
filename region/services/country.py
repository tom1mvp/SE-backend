from region.repositories.country import CountryRepository

class CountryServices:
    """
    Country Management Service Layer

    Acts as an intermediary between the API views and the Country Repository.
    Encapsulates business logic for retrieving geographic master data.

    Methods:
    - GET:
        * Fetch all countries for global listings.
        * Search countries by specific criteria (ID or Name).
    """
    
    @staticmethod
    def get_all_country():
        # Delegate retrieval of all countries to the repository
        return CountryRepository.get_all_country()
    
    @staticmethod
    def get_country_by_id(country_id):
        # Resolve a single country instance by its unique identifier
        return CountryRepository.get_country_by_id(country_id)
    
    @staticmethod
    def get_country_by_name(country_name):
        # Handle search logic for countries based on naming conventions
        return CountryRepository.get_country_by_name(country_name)