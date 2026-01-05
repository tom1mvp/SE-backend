"""
Institution Management Repository

This module acts as the central orchestrator for educational entities. It handles 
the creation, retrieval, and life-cycle updates of institutions, managing 
complex joins between physical addresses, administrative categories, 
and academic periods.

Key Features:
- Geographical Filtering: Search institutions by city through address relations.
- Integrity Checks: Validates existence of linked entities (Address, Category, Cycle).
- Status Management: Implements logical deletion (deactivation) and recovery.
- Cycle Updates: Allows for automatic transitions between academic years.
"""

from establishment.models import Institution, Address, InstitutionCategory
from academic.models import ElectiveCycle


class InstitutionRepository:
    @staticmethod
    def get_all_institution():
        # Retrieves the complete directory of registered institutions.
        return Institution.objects.all()
    
    @staticmethod
    def get_institution_by_id(institution_id):
        # Fetches a specific institution record by its unique primary key.
        return Institution.objects.filter(id=institution_id).first()
    
    @staticmethod
    def get_institution_by_name(name):
        # Performs a case-insensitive search to find institutions by name.
        return Institution.objects.filter(name__icontains=name).first()
    
    @staticmethod
    def get_institution_by_city(city_name):
        # Joins Institution and Address tables to filter by a specific city.
        return Institution.objects.filter(address__city__name__icontains=city_name)
    
    @staticmethod
    def get_institution_by_category(category_name):
        return Institution.objects.filter(category__name__icontains=category_name)
    
    @staticmethod
    def create_institution(
        name,
        opening_hour,
        closing_hour,
        logo_url,
        category_id,
        address_id,
        elective_cycle_id,
        is_active=True
    ):
        # Validates that the physical address exists before linking.
        address = Address.objects.filter(id=address_id).first()
        
        if not address:
            raise ValueError('Error', 'Not found address')
        
        # Ensures the assigned category is valid and registered.
        category = InstitutionCategory.objects.filter(id=category_id).first()
        
        if not category:
            raise ValueError('Error', 'Category not found')
        
        # Verifies that the starting academic cycle is correctly defined.
        elective_cycle = ElectiveCycle.objects.filter(id=elective_cycle_id).first()
        
        if not elective_cycle:
            raise ValueError('Error', 'Elective cycle not found')
        
        # Persists the new institution with all mandatory relational dependencies.
        new_institution = Institution.objects.create(
            name=name,
            opening_hour=opening_hour,
            closing_hour=closing_hour,
            logo_url=logo_url,
            category=category,
            address=address,
            elective_cycle=elective_cycle,
            is_active=is_active
        )
        
        return new_institution
    
    @staticmethod
    def update_institution(
        institution_id,
        name,
        opening_hour,
        closing_hour,
        logo_url,
        category_id,
        address_id,
    ):
        # Locates the existing institution to be modified.
        institution = Institution.objects.filter(id=institution_id).first()
        
        if not institution:
            raise ValueError('Error', 'Institution not found')
        
        # Validates potential changes in the physical location link.
        address = Address.objects.filter(id=address_id).first()
        
        if not address:
            raise ValueError('Error', 'Not found address')
        
        # Validates potential changes in the institution classification.
        category = InstitutionCategory.objects.filter(id=category_id).first()
        
        if not category:
            raise ValueError('Error', 'Category not found')
        
        # Synchronizes all updated attributes with the database.
        institution.name=name
        institution.opening_hour=opening_hour
        institution.closing_hour=closing_hour
        institution.logo_url=logo_url
        institution.category=category
        institution.address=address
        
        institution.save()
        
        return institution
    
    @staticmethod
    def update_elective_cycle_automatic(institution_id, elective_cycle_id):
        # Locates the institution for the automatic cycle transition.
        institution = Institution.objects.filter(id=institution_id).first()
        
        if not institution:
            raise ValueError('Error', 'Institution not found')
        
        # Ensures the new academic cycle exists before the update.
        elective_cycle = ElectiveCycle.objects.filter(id=elective_cycle_id).first()
        
        if not elective_cycle:
            raise ValueError('Error', 'Elective cycle not found')
        
        # Updates the institution context to the new school year.
        institution.elective_cycle = elective_cycle
        
        institution.save()
        
        return institution
    
    @staticmethod
    def delete_institution(institution_id):
        # Locates the institution to perform a logical deactivation.
        institution = Institution.objects.filter(id=institution_id).first()
        
        if not institution:
            raise ValueError('Error', 'Institution not found')
        
        # Sets the active status to false to restrict system access.
        if institution.is_active:
            institution.is_active = False
            
            institution.save()
        
            return institution
        
    @staticmethod
    def recover_institution(institution_id):
        # Locates a deactivated institution for restoration.
        institution = Institution.objects.filter(id=institution_id).first()
        
        if not institution:
            raise ValueError('Error', 'Institution not found')
        
        # Re-enables the institution to restore operational status.
        if institution.is_active == False:
            institution.is_active= True
            
            institution.save()
        
            return institution