from grades.models import Grade, AssessmentCategory
from academic.models import Subject
from student_institution.models import Student


"""
    Grade Repository
    
    This module manages the persistence of student grades.
    It provides a standardized interface for retrieving, creating, 
    and updating academic marks, ensuring data integrity between 
    students, subjects, and their respective evaluation categories.
"""

class GradeRepository:

    # Retrieves all existing grade records from the database.
    @staticmethod
    def get_all_grades():
        return Grade.objects.all()
    
    # Retrieves all grades associated with a specific subject name.
    @staticmethod
    def get_grades_by_subject(name):
        return Grade.objects.filter(subject__name__icontains=name)
    
    # Retrieves all grades belonging to a specific academic term (e.g., "primero").
    @staticmethod
    def get_grades_by_term(term):
        return Grade.objects.filter(term__icontains=term)
    
    @staticmethod
    def get_grades_by_student(name):
        return Grade.objects.filter(student__person__first_name__icontains=name)
    
    # Persists a new grade record after validating subject, student, and category existence.
    @staticmethod
    def create_grade(
        number,
        date,
        term,
        subject_id,
        student_id,
        category_id
    ):
        subject = Subject.objects.filter(id=subject_id).first()
        if not subject:
            raise ValueError('Subject not found')
        
        student = Student.objects.filter(id=student_id).first()
        if not student:
            raise ValueError('Student not found')
        
        category = AssessmentCategory.objects.filter(id=category_id).first()
        if not category:
            raise ValueError('Category not found')
        
        # Creates the grade record with the validated instances.
        new_grade = Grade.objects.create(
            number=number,
            date=date,
            term=term,
            subject=subject,
            student=student,
            category=category
        )
        
        return new_grade
    
    # Updates an existing grade record and refreshes its relations.
    @staticmethod
    def update_grade(
        grade_id,
        number,
        date,
        term,
        subject_id,
        student_id,
        category_id
    ):
        grade = Grade.objects.filter(id=grade_id).first()
        if not grade:
            raise ValueError('Grade not found')
        
        subject = Subject.objects.filter(id=subject_id).first()
        if not subject:
            raise ValueError('Subject not found')
        
        student = Student.objects.filter(id=student_id).first()
        if not student:
            raise ValueError('Student not found')
        
        category = AssessmentCategory.objects.filter(id=category_id).first()
        if not category:
            raise ValueError('Category not found')
        
        # Updates the fields and persists changes to the database.
        grade.number = number
        grade.date = date
        grade.term = term
        grade.subject = subject
        grade.student = student
        grade.category = category
        
        
        grade.save()
        
        return grade