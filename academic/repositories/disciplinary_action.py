from academic.models import DisciplinaryAction
from student_institution.models import Student

"""
    Academic Disciplinary Action Repository
    
    This module handles the persistence layer for student disciplinary records.
    It encapsulates all direct ORM queries, providing a clean interface for 
    creating, searching, and updating sanctions while maintaining data integrity.
"""

class DisciplinaryActionRepository:
    # Retrieves every disciplinary record stored in the database.
    @staticmethod
    def get_all_disciplinary_action():
        return DisciplinaryAction.objects.all()
    
    # Filters records based on the specific calendar date of the incident.
    @staticmethod
    def get_disciplinary_action_by_date(date):
        return DisciplinaryAction.objects.filter(date=date)
    
    # Performs a lookup based on a partial match of the student's first name.
    @staticmethod
    def get_disciplinary_action_by_student(name):
        return DisciplinaryAction.objects.filter(student__person__first_name__icontains=name).first()
    
    # Handles the creation of a new disciplinary entry, ensuring student linkage.
    @staticmethod
    def create_disciplinary_action(
        date,
        reason,
        quantity,
        observation,
        student_id
    ):
        # Validates that the student exists before assigning a sanction.
        student = Student.objects.filter(id=student_id).first()
        
        if not student:
            raise ValueError('error', 'Student not found')
        
        # Persists the validated incident data into the database.
        new_disciplinary_action = DisciplinaryAction.objects.create(
            date=date,
            reason=reason,
            quantity=quantity,
            observation=observation,
            student=student
        )
        
        return new_disciplinary_action
    
    # Coordinates the modification of existing conduct records.
    @staticmethod
    def update_disciplinary_action(
        disciplinary_action_id,
        date,
        reason,
        quantity,
        observation,
        student_id
    ):
        # Locates the specific sanction record for update.
        disciplinary_action = DisciplinaryAction.objects.filter(id=disciplinary_action_id).first()
        
        if not disciplinary_action:
            raise ValueError('Disciplinary action not found')
        
        # Ensures the updated record remains linked to a valid student.
        student = Student.objects.filter(id=student_id).first()
        
        if not student:
            raise ValueError('Student not found')
        
        # Atomic field updates.
        disciplinary_action.date = date
        disciplinary_action.reason = reason
        disciplinary_action.quantity = quantity
        disciplinary_action.observation = observation
        disciplinary_action.student = student
        
        # Commits the changes to ensure persistence.
        disciplinary_action.save()
        
        return disciplinary_action