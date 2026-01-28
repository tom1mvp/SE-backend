from rest_framework.validators import ValidationError


from academic.repositories.disciplinary_action import DisciplinaryActionRepository


"""
    Disciplinary Action Service Layer
    
    This module manages the business logic for student conduct and disciplinary records.
    It serves as an abstraction layer that validates behavioral data and coordinates 
    with the repository to maintain a reliable history of institutional sanctions.
"""

class DisciplinaryActionServices:
    # Provides access to the full historical record of all disciplinary actions.
    @staticmethod
    def get_all_disciplinary_action():
        return DisciplinaryActionRepository.get_all_disciplinary_action()
    
    # Retrieves disciplinary incidents that occurred on a specific calendar date.
    @staticmethod
    def get_disciplinary_action_by_date(date):
        return DisciplinaryActionRepository.get_disciplinary_action_by_date(date)
    
    # Locates conduct records for a specific student based on their identifying name/criteria.
    @staticmethod
    def get_disciplinary_action_by_student(name):
        return DisciplinaryActionRepository.get_disciplinary_action_by_student(name)
    
    # Handles the logic for registering a new sanction, ensuring all mandatory data is present.
    @staticmethod
    def create_disciplinary_action(data, student_id):
        # Mandatory attributes required to document a disciplinary incident.
        required_fields = [
            'date',
            'reason',
            'quantity',
            'observation'
        ]
        
        # Validation Loop: Ensures the payload contains all necessary institutional data.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        # Commits the new disciplinary record to the database via the repository.
        new_disciplinary_action = DisciplinaryActionRepository.create_disciplinary_action(
            date=data['date'],
            reason=data['reason'],
            quantity=data['quantity'],
            observation=data['observation'],
            student_id=student_id
        )
        
        return new_disciplinary_action
    
    # Manages the modification of existing sanctions while preserving data integrity.
    @staticmethod
    def update_disciplanry_action(data, disciplinary_action_id, student_id):
        required_fields = [
            'date',
            'reason',
            'quantity',
            'observation'
        ]
        
        # Validates that the update request meets the required data schema.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        # Triggers the repository update for the specified disciplinary record.
        disciplinary_action = DisciplinaryActionRepository.update_disciplinary_action(
            disciplinary_action_id=disciplinary_action_id,
            date=data['date'],
            reason=data['reason'],
            quantity=data['quantity'],
            observation=data['observation'],
            student_id=student_id
        )
        
        return disciplinary_action