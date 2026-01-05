"""
Institution Category Management Service

This service provides the business logic layer for institutional 
classifications. It acts as an intermediary between the controllers 
and the repository, ensuring standardized access to categories like 
'Public', 'Private', or 'Technical' across the system.

Business Logic:
- Standardization: Centralizes the retrieval of administrative categories.
- Search Flexibility: Allows finding classifications by unique IDs or names.
"""

from establishment.repositories.institution_category import InstitutionCategoryRepository


class InstitutionCategoryServices:
    @staticmethod
    def get_all_category():
        # Orchestrates the retrieval of the complete category list.
        return InstitutionCategoryRepository.get_all_category()
    
    @staticmethod
    def get_category_by_id(category_id):
        # Coordinates the search for a specific category via its identifier.
        return InstitutionCategoryRepository.get_category_by_id(category_id)
    
    @staticmethod
    def get_category_by_name(name):
        # Manages the query for categories based on their descriptive name.
        return InstitutionCategoryRepository.get_category_by_name(name)