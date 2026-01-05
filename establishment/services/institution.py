"""
Institution Management Service

This service acts as the primary orchestrator for educational entities. It 
manages the business rules for creating and updating institutions, ensuring 
that all operational data like hours and logos are validated before being 
linked to their physical addresses and academic cycles.

Business Logic:
- Integrity Validation: Ensures all core institutional fields are provided.
- State Management: Coordinates logical deletion and recovery of entities.
- Academic Continuity: Manages the automatic transition between elective cycles.
- Multi-domain Linking: Bridges the gap between Category, Address, and Cycle domains.
"""

from rest_framework.validators import ValidationError


from establishment.repositories.institution import InstitutionRepository


class InstitutionServices:
    @staticmethod
    def get_all_institution():
        # Proxies the request to retrieve the complete list of institutions.
        return InstitutionRepository.get_all_institution()
    
    @staticmethod
    def get_institution_by_id(institution_id):
        # Fetches a specific institution using its unique identifier.
        return InstitutionRepository.get_institution_by_id(institution_id)
    
    @staticmethod
    def get_institution_by_name(name):
        # Searches for institutions based on their descriptive name.
        return InstitutionRepository.get_institution_by_name(name)
    
    @staticmethod
    def get_institution_by_city(city_name):
        # Filters institutions based on their geographical city location.
        return InstitutionRepository.get_institution_by_city(city_name)
    
    @staticmethod
    def get_institution_by_category(category_name):
        return InstitutionRepository.get_institution_by_category(category_name)
    
    @staticmethod
    def create_institution(
        data,
        category_id,
        address_id,
        elective_cycle_id
    ):
        # Defines the set of mandatory attributes for an educational entity.
        required_fields = [
            'name',
            'opening_hour',
            'closing_hour',
            'logo_url',
        ]
        
        # Validates that the input payload contains all necessary business data.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        # Coordinates with the repository to persist the new institution record.
        new_institution = InstitutionRepository.create_institution(
            name=data['name'],
            opening_hour=data['opening_hour'],
            closing_hour=data['closing_hour'],
            logo_url=data['logo_url'],
            category_id=category_id,
            address_id=address_id,
            elective_cycle_id=elective_cycle_id
        )
        
        return new_institution
    
    @staticmethod
    def update_institution(
        data,
        institution_id,
        category_id,
        address_id,
        elective_cycle_id
    ):
        # Core fields required for a consistent institutional profile.
        required_fields = [
            'name',
            'opening_hour',
            'closing_hour',
            'logo_url',
        ]
        
        # Ensures that the update request maintains data integrity rules.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
            
        # Triggers the update process for the specified institution.
        institution = InstitutionRepository.update_institution(
            institution_id=institution_id,
            name=data['name'],
            opening_hour=data['opening_hour'],
            closing_hour=data['closing_hour'],
            logo_url=data['logo_url'],
            category_id=category_id,
            address_id=address_id,
            elective_cycle_id=elective_cycle_id
        )
        
        return institution
    
    @staticmethod
    def update_elective_cycle_automatic(institution_id, elective_cycle_id):
        # Automates the shift of an institution to a new academic period.
        return InstitutionRepository.update_elective_cycle_automatic(institution_id, elective_cycle_id)
    
    @staticmethod
    def delete_institution(institution_id):
        # Performs a logical deletion to deactivate the institutional record.
        return InstitutionRepository.delete_institution(institution_id)
    
    @staticmethod
    def recover_elective_cycle(institution_id):
        # Restores a previously deactivated institution to active status.
        return InstitutionRepository.recover_institution(institution_id)