"""
Institution Category Management Repository

This module handles the persistence logic for classifying educational 
entities. It manages the different institutional profiles (e.g., Public, 
Private, Technical, Secondary) to ensure standardized categorization 
across the entire school system.

Core Responsibilities:
- Category Retrieval: Accessing classifications by ID or specific names.
- Data Consistency: Providing unique identification for institution types.
"""

from establishment.models import InstitutionCategory


class InstitutionCategoryRepository:
    
    @staticmethod
    def get_all_category():
        # Retrieves the complete list of available institution classifications.
        return InstitutionCategory.objects.all()

    @staticmethod
    def get_category_by_id(category_id):
        # Fetches a specific category using its primary key for relational lookups.
        return InstitutionCategory.objects.filter(id=category_id).first()
    
    @staticmethod
    def get_category_by_name(name):
        # Performs a case-insensitive search to find a category by its name.
        # Uses __icontains to allow partial matches in administrative searches.
        return InstitutionCategory.objects.filter(name__icontains=name).first()