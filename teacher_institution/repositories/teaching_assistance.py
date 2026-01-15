from teacher_institution.models import TeachingAssistance, Teacher


class TeachingAssistanceRepository:
    """
    Repository class to manage data access logic for Teacher Attendance and Assistance records.
    This layer abstracts the ORM queries, providing a centralized API for 
    tracking staff presence, absences, and justifications.
    """

    @staticmethod
    def get_all_teaching_assistance():
        """
        Retrieves all assistance records stored in the database.
        Useful for generating global attendance reports or administrative overviews.
        """
        return TeachingAssistance.objects.all()
    
    @staticmethod
    def get_teaching_assistance_by_id(teaching_assistance_id):
        """
        Fetches a specific assistance record by its unique primary key.
        Returns None if the ID does not exist to allow for graceful error handling in services.
        """
        return TeachingAssistance.objects.filter(id=teaching_assistance_id).first()
    
    @staticmethod
    def get_teaching_assistance_by_name(name):
        """
        Filters attendance records based on the teacher's first name.
        Uses a join-like lookup (teacher__person__first_name) to reach the Person 
        attributes through the Teacher relationship.
        """
        
        return TeachingAssistance.objects.filter(teacher__person__first_name__icontains=name).first()
    
    @staticmethod
    def get_teaching_assistance_by_date(date):
        """
        Retrieves all assistance records for a specific calendar date.
        This is critical for daily presence checks and institutional monitoring.
        """
        return TeachingAssistance.objects.filter(date=date)
    
    @staticmethod
    def create_teaching_assistance(
      date,
      reason,
      observation,
      teacher_id 
    ):
        """
        Handles the creation of a new attendance entry.
        It verifies the existence of the Teacher entity before persisting the record 
         to maintain data integrity and prevent foreign key violations.
        """
        # Verification of the teacher record
        teacher = Teacher.objects.filter(id=teacher_id).first()
        
        if not teacher:
            raise ValueError('Error', 'Teacher not found')
        
        # Persistence of the new assistance entry
        new_teaching_assistance = TeachingAssistance.objects.create(
            date=date,
            reason=reason,
            observation=observation,
            teacher=teacher
        )
        
        return new_teaching_assistance
    
    @staticmethod
    def update_teaching_assistance(
        teaching_assistance_id,
        date,
        reason,
        observation,
        teacher_id
    ):
        """
        Updates an existing attendance record.
        This method performs a full update of the entry's attributes and 
        re-validates the teacher relationship to ensure the data remains accurate.
        """
        # Lookup for the existing record
        assistance = TeachingAssistance.objects.filter(id=teaching_assistance_id).first()
        
        if not assistance:
            raise ValueError('Error', 'Teaching assistance record not found')
        
        # Validation of the associated teacher
        teacher = Teacher.objects.filter(id=teacher_id).first()
        
        if not teacher:
            raise ValueError('Error', 'Teacher not found')
        
        # Updating attributes
        assistance.date = date
        assistance.reason = reason
        assistance.observation = observation
        
        assistance.save()
        
        return assistance