from rest_framework.validators import ValidationError


from grades.repositories.assessment_category import AssessmentCategoryRepository


"""
    Assessment Category Services
    
    This module implements the business logic for grading categories.
    It acts as a middle layer between the API views and the repository,
    handling data validation and ensuring that only compliant information
    is processed by the persistence layer.
"""

class AssessmentCategoryServices:

    # Orchestrates the retrieval of all assessment categories through the repository.
    @staticmethod
    def get_all_assessment_category():
        return AssessmentCategoryRepository.get_all_assessment_category()
    
    # Validates input data and coordinates the creation of a new assessment category.
    @staticmethod
    def create_assessment_category(data):
        # List of essential attributes required to define an assessment category.
        required_fields = ['name']
        
        # Data Integrity Check: Verify that all required fields are present in the request payload.
        for field in required_fields:
            if field not in data:
                # Raises a standardized validation error if a mandatory field is missing.
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        # Proceeds to creation once the payload integrity is confirmed.
        new_assessment_category = AssessmentCategoryRepository.create_assessment_category(
            name=data['name']
        )
        
        return new_assessment_category