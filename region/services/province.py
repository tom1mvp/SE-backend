from region.repositories.province import ProvinceRepository

class ProvinceServices:
    """
    Province Management Service Layer

    Acts as an intermediary between the API views and the Province Repository.
    Handles business logic for regional data retrieval and stratification.

    Methods:
    - GET:
        * Fetch all provinces or filter them by country association.
        * Search provinces by specific criteria (ID or Name).
    """
    
    @staticmethod
    def get_all_provinces():
        # Delegate retrieval of the complete province list to the repository
        return ProvinceRepository.get_all_province()
    
    @staticmethod
    def get_province_by_id(province_id):
        # Resolve a specific province instance by its unique identifier
        return ProvinceRepository.get_province_by_id(province_id)
    
    @staticmethod
    def get_province_by_name(province_name):
        # Handle search logic for provinces based on name matches
        return ProvinceRepository.get_province_by_name(province_name)
    
    @staticmethod
    def get_province_by_country(country_id):
        # Retrieve all provinces belonging to a specific country
        return ProvinceRepository.get_province_by_country(country_id)