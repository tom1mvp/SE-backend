from region.models import Country

class CountryRepository:
    """
    Country Management Repository

    Provides read-only access to the geographic master data. 
    Mainly used as a global reference for addressing, localization, 
    and regional filtering across the platform.

    Methods:
    - GET:
        * List all registered countries (supports pagination and alphabetical sorting).
        * Search by name prefixes or partial matches for autocomplete features.
        * Retrieve a specific country instance by ID (Primary Key) to resolve relationships.
    """
    
    @staticmethod
    def get_all_country():
        # returns all countries
        return Country.objects.all()
    
    @staticmethod
    def get_country_by_id(country_id):
        # return country by id
        return Country.objects.filter(id=country_id).first()
    
    @staticmethod
    def get_country_by_name(country_name):
        # return country by name
        return Country.objects.filter(name__icontains=country_name).first()