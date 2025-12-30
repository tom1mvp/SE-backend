from region.models import Province

class ProvinceRepository:
    """
    Province Management Repository

    Provides read-only access to state and provincial data.
    Facilitates regional stratification by linking localities to their 
    respective countries.

    Methods:
    - GET:
        * List all provinces (globally or filtered by country).
        * Search provinces by name for regional selection.
        * Retrieve a specific province by ID to access its country relationship.
    """
    
    @staticmethod
    def get_all_province():
        # Retrieve all provinces registered in the system
        return Province.objects.all()
    
    @staticmethod
    def get_province_by_id(province_id):
        # Find a specific province by its primary key
        return Province.objects.filter(id=province_id).first()
    
    @staticmethod
    def get_province_by_name(province_name):
        # Filter provinces by name using case-insensitive partial match
        return Province.objects.filter(name__icontains=province_name).first()
    
    @staticmethod
    def get_province_by_country(country_id):
        # List all provinces associated with a specific country ID
        return Province.objects.filter(country=country_id)
    
    