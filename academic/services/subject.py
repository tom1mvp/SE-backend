from datetime import time, datetime


from rest_framework.validators import ValidationError
from academic.repositories.subject import SubjectRepository

class SubjectServices:
    """
    Service layer for Subject management.
    Handles business rules, time-range validations, and orchestrates data 
    transfer between the API and Repository layers.
    """

    @staticmethod
    def get_all_subject():
        # Retrieves all subject records via the Repository.
        return SubjectRepository.get_all_subject()
    
    @staticmethod
    def get_subject_by_name(subject_name):
        # Business logic for name-based subject retrieval.
        return SubjectRepository.get_subject_by_name(subject_name)
    
    @staticmethod
    def get_subject_by_course(course_name):
        # Filters subjects associated with a specific course name.
        return SubjectRepository.get_subject_by_course(course_name)
    
    @staticmethod
    def create_subject(data, course_id, teacher_id):
        """
        Coordinates the creation of a Subject.
        Validates mandatory fields and ensures the time range is logical.
        """
        # List of required fields for subject creation.
        required_fields = ['name', 'start_time', 'end_time']
        
        # Data Integrity Check: Ensure all fields are present in the payload.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        start_time_val = data.get('start_time')
        end_time_val = data.get('end_time')
        
        try:
            start_time_val = datetime.strptime(data.get('start_time'), '%H:%M:%S').time()
            end_time_val = datetime.strptime(data.get('end_time'), '%H:%M:%S').time()
        except ValueError:
            raise ValidationError({"error": "Invalid time format. Use HH:MM:SS"})
        
        # Business Rule: Prevent invalid time ranges where end precedes start.
        if start_time_val and end_time_val and end_time_val <= start_time_val:
            raise ValidationError({
                "end_time": "The end time must be later than the start time."
            })
        
        # Business Rule: Validate against institutional operating hours (07:00 - 22:00).
        if start_time_val and (start_time_val < time(7, 0) or start_time_val > time(22, 0)):
            raise ValidationError({
                "start_time": "The start time must be between 7:00 a.m. and 10:00 p.m."
            })
        
        # Invokes repository to persist the new subject.
        return SubjectRepository.create_subject(
            name=data['name'],
            start_time=start_time_val, 
            end_time=end_time_val,
            course_id=course_id,
            teacher_id=teacher_id
        )
    
    @staticmethod
    def update_subject(data, subject_id, course_id, teacher_id):
        """
        Coordinates the update process for an existing subject.
        Re-validates business constraints to ensure data consistency.
        """
        required_fields = ['name', 'start_time', 'end_time']
        
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        start_time_val = data.get('start_time')
        end_time_val = data.get('end_time')
        
        try:
            start_time_val = datetime.strptime(data.get('start_time'), '%H:%M:%S').time()
            end_time_val = datetime.strptime(data.get('end_time'), '%H:%M:%S').time()
        except ValueError:
            raise ValidationError({"error": "Invalid time format. Use HH:MM:SS"})
        
        if start_time_val and end_time_val and end_time_val <= start_time_val:
            raise ValidationError({
                "end_time": "The end time must be later than the start time."
            })
        
        if start_time_val and (start_time_val < time(7, 0) or start_time_val > time(22, 0)):
            raise ValidationError({
                "start_time": "The start time must be between 7:00 a.m. and 10:00 p.m."
            })
        
        # Invokes repository to update the existing record.
        return SubjectRepository.update_subject(
            subject_id=subject_id,
            name=data['name'],
            start_time=start_time_val,
            end_time=end_time_val,
            course_id=course_id,
            teacher_id=teacher_id
        )
    
    @staticmethod
    def delete_subject(subject_id):
        # Triggers logical deletion via the repository.
        return SubjectRepository.delete_subject(subject_id)
    
    @staticmethod
    def recover_subject(subject_id):
        # Restores a previously deactivated subject.
        return SubjectRepository.recover_subject(subject_id)