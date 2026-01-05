"""
Address Management Repository

This module handles the persistence logic for physical locations within 
the establishment domain. It serves as the bridge between raw location 
data and the geographical relational structure (Cities and Regions), 
ensuring that every establishment or entity has a validated physical point.

Key Responsibilities:
- Spatial Data Retrieval: Fetching addresses by street, city, or ID.
- Relational Integrity: Ensuring that every address is linked to a valid City.
- Maintenance: Coordinating updates and creation of physical records.
"""

from establishment.models import Address
from region.models import City


class AddressRepository:
    
    @staticmethod
    def get_all_address():
        # Retrieves the complete directory of registered addresses.
        return Address.objects.all()
    
    @staticmethod
    def get_address_by_id(address_id):
        # Fetches a specific address record by its primary key.
        return Address.objects.filter(id=address_id).first()
    
    @staticmethod
    def get_address_by_street(street):
        # Performs a search based on the street name for location matching.
        return Address.objects.filter(street__icontains=street).first()
    
    @staticmethod
    def get_address_by_city(city_id):
        # Filters all addresses belonging to a specific administrative city.
        return Address.objects.filter(city=city_id)
    
    @staticmethod
    def create_address(
        street,
        number,
        comment,
        city_id
    ):
        # Validates the existence of the city before linkind the new location.
        city = City.objects.filter(id=city_id).first()
        
        if not city:
            raise ValueError('Error', 'City not found')
        
        # Persists the new physical record in the database.
        new_address = Address.objects.create(
            street=street,
            number=number,
            comment=comment,
            city=city
        )
        
        return new_address
    
    @staticmethod
    def update_address(
        address_id,
        street,
        number,
        comment,
        city_id
    ):
        # Locates the existing address to be modified.
        address = Address.objects.filter(id=address_id).first()
        
        if not address:
            raise ValueError('Error', 'Address not found')
        
        # Validates the new city reference to maintain data integrity.
        city = City.objects.filter(id=city_id).first()
        
        if not city:
            raise ValueError('Error', 'City not found')
        
        # Updates the object attributes and synchronizes with the database.
        address.street = street
        address.number = number
        address.comment = comment
        address.city = city
        
        address.save()
        
        return address