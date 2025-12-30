from region.repositories.city import CityRepository

class CityServices:
    """
    City Management Service Layer

    Acts as an intermediary between the API views and the City Repository.
    Manages the final level of geographic granularity for the system.

    Methods:
    - GET:
        * Fetch all cities or filter them by province association.
        * Search cities by name for address selection.
        * Resolve specific city instances by ID.
    """
    
    @staticmethod
    def get_all_city():
        # Delegate retrieval of all registered cities to the repository
        return CityRepository.get_all_city()
    
    @staticmethod
    def get_city_by_id(city_id):
        # Resolve a specific city instance by its primary key
        return CityRepository.get_city_by_id(city_id)
    
    @staticmethod
    def get_city_by_name(city_name):
        # Handle search logic for cities based on name matches
        return CityRepository.get_city_by_name(city_name)
    
    @staticmethod
    def get_city_by_province(province_id):
        # Retrieve all cities belonging to a specific province
        return CityRepository.get_city_by_province(province_id)
    
    