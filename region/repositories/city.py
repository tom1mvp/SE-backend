from region.models import City

class CityRepository:
    """
    City Management Repository

    Provides read-only access to city and locality data.
    Acts as the final level of geographic granularity, linking 
    specific urban areas to their parent provinces.

    Methods:
    - GET:
        * List all cities (globally or filtered by province).
        * Search by name for address completion and geolocation.
        * Retrieve a specific city by ID to resolve its full administrative hierarchy.
    """
    
    @staticmethod
    def get_all_city():
        # Retrieve all cities registered in the system
        return City.objects.all()
    
    @staticmethod
    def get_city_by_id(city_id):
        # Find a specific city by its primary key
        return City.objects.filter(id=city_id).first()
    
    @staticmethod
    def get_city_by_name(city_name):
        # Filter cities by name using case-insensitive partial match
        return City.objects.filter(name__icontains=city_name).first()
    
    @staticmethod
    def get_city_by_province(province_id):
        # List all cities associated with a specific province ID
        return City.objects.filter(province=province_id)