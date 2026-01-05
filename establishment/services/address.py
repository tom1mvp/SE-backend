"""
Address Management Service

This service acts as the business logic layer for physical locations. It 
orchestrates the validation of mandatory fields before persistence and 
manages the communication with the AddressRepository to ensure data 
consistency across the establishment domain.

Business Logic:
- Data Validation: Ensures 'street', 'number', and 'comment' are present.
- Integrity: Coordinates with city identifiers to link physical addresses.
- Access Control: Provides methods for filtered retrieval by city or street.
"""

from rest_framework.validators import ValidationError


from establishment.repositories.address import AddressRepository


class AddressServices:
    @staticmethod
    def get_all_address():
        # Proxies the request to retrieve the full directory of addresses.
        return AddressRepository.get_all_address()
    
    @staticmethod
    def get_address_by_id(address_id):
        # Fetches a specific address by its unique identifier.
        return AddressRepository.get_address_by_id(address_id)
    
    @staticmethod
    def get_address_by_street(street):
        # Retrieves address information based on the street name.
        return AddressRepository.get_address_by_street(street)
    
    @staticmethod
    def get_address_by_city(city_id):
        # Filters and returns all addresses registered within a specific city.
        return AddressRepository.get_address_by_city(city_id)
    
    @staticmethod
    def create_address(
        data,
        city_id
    ):
        # List of attributes required to maintain institutional records.
        required_fields = [
            'street',
            'number',
            'comment'
        ]
        
        # Validation loop to ensure no mandatory data is missing from the payload.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        # Triggers the persistence logic through the repository layer.
        new_address = AddressRepository.create_address(
            street=data['street'],
            number=data['number'],
            comment=data['comment'],
            city_id=city_id
        )
        
        return new_address
    
    @staticmethod
    def update_address(
        data,
        address_id,
        city_id
    ):
        # Mandatory fields check for the update process.
        required_fields = [
            'street',
            'number',
            'comment'
        ]
        
        # Validates that the update payload contains all necessary information.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        # Synchronizes the modifications with the existing record via repository.
        address = AddressRepository.update_address(
            address_id,
            street=data['street'],
            number=data['number'],
            comment=data['comment'],
            city_id=city_id
        )
        
        return address