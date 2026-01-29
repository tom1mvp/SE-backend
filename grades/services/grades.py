from rest_framework.validators import ValidationError
from grades.repositories.grades import GradeRepository


"""
    Grade Services
    
    This module implements the business logic for student grades.
    It serves as the intermediary layer that validates grade ranges, 
    term consistency, and payload integrity before interacting 
    with the Grade Repository.
"""


class GradeServices:

    # Orchestrates the retrieval of all grade records through the repository.
    @staticmethod
    def get_all_grades():
        return GradeRepository.get_all_grades()
    
    # Coordinates the search for grade records filtered by a specific subject name.
    @staticmethod
    def get_grade_by_subject(name):
        return GradeRepository.get_grades_by_subject(name)
    
    # Coordinates the search for grade records filtered by academic term.
    @staticmethod
    def get_grade_by_term(term):
        return GradeRepository.get_grades_by_term(term)
    
    @staticmethod
    def get_grade_by_student(name):
        return GradeRepository.get_grades_by_student(name)
    
    # Validates input data and coordinates the creation of a new grade record.
    @staticmethod
    def create_grade(data, subject_id, student_id, category_id):
        # List of essential attributes required for a grade record.
        required_fields = ['number', 'date', 'term']
        
        # Data Integrity Check: Verify that all required fields are present in the request payload.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'The field {field} is mandatory.'})
        
        # Business Logic Validation: Ensure the grade value remains within the 0-10 range.
        if not (0 <= data['number'] <= 10):
            raise ValidationError({'number': 'The grade must be between 0 and 10.'})
            
        # Forwards validated data to the repository for persistence.
        new_grade = GradeRepository.create_grade(
            number=data['number'],
            date=data['date'],
            term=data['term'],
            subject_id=subject_id,
            student_id=student_id,
            category_id=category_id
        )
        
        return new_grade
    
    # Validates and coordinates the update process for an existing grade record.
    @staticmethod
    def update_grade(data, grade_id, subject_id, student_id, category_id):
        # List of essential attributes required for updating a grade record.
        required_fields = ['number', 'date', 'term']
        
        # Data Integrity Check: Verify that all required fields are present in the request payload.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'The field {field} is mandatory.'})

        # Business Logic Validation: Ensure the updated grade value remains within the 0-10 range.
        if not (0 <= data['number'] <= 10):
            raise ValidationError({'number': 'The grade must be between 0 and 10.'})
        
        # Coordinates the update operation through the repository.
        grade = GradeRepository.update_grade(
            grade_id=grade_id,
            number=data['number'],
            date=data['date'],
            term=data['term'],
            subject_id=subject_id,
            student_id=student_id,
            category_id=category_id
        )
        
        return grade