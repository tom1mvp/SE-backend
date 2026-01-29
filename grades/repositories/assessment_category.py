from grades.models import AssessmentCategory


"""
    Assessment Category Repository
    
    This module manages the persistence of grading categories.
    It provides a standardized interface for retrieving and creating
    different evaluation methods (e.g., "Examen", "TP"), ensuring 
    consistency across the grade tracking system.
"""

class AssessmentCategoryRepository:

    # Retrieves all existing evaluation categories from the database.
    @staticmethod
    def get_all_assessment_category():
        return AssessmentCategory.objects.all()
    
    # Persists a new assessment category in the database using the provided name.
    @staticmethod
    def create_assessment_category(name):
        # Creates a new record using the provided category name.
        new_assessment_category = AssessmentCategory.objects.create(
            name=name
        )
        
        return new_assessment_category