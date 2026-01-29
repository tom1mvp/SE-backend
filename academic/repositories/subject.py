"""
This module implements the Repository Pattern for the Subject entity. 
Includes advanced Soft Delete and Recovery mechanisms for data lifecycle management.
"""

from academic.models import Subject, Course
from teacher_institution.models import Teacher


class SubjectRepository:
    """
    Data Access Layer for the Subject model.
    Optimizes database interactions and ensures business integrity at the persistence level.
    """

    @staticmethod
    def get_all_subject():
        # Retrieves all Subject records.
        return Subject.objects.all()
    
    @staticmethod
    def get_subject_by_name(subject_name):
        # Case-insensitive partial match search.
        return Subject.objects.filter(name__icontains=subject_name).first()
    
    @staticmethod
    def get_subject_by_course(course_name):
        # Relationship-based filtering via Course entity.
        return Subject.objects.filter(course__name__icontains=course_name)
    
    @staticmethod
    def create_subject(name, start_time, end_time, course_id, teacher_id, is_active=True):
        # Persists a new Subject linked to a validated Course.
        course = Course.objects.filter(id=course_id).first()
        if not course:
            raise ValueError('error' ,'Associated Course not found')
        
        teacher = Teacher.objects.filter(id=teacher_id).first()
        
        if not teacher:
            raise ValueError('error' ,'Teacher not found')
        
        return Subject.objects.create(
            name=name,
            start_time=start_time,
            end_time=end_time,
            is_active=is_active,
            course=course,
            teacher=teacher
        )
    
    @staticmethod
    def update_subject(
        subject_id, 
        name, 
        start_time, 
        end_time, 
        course_id, 
        teacher_id
    ):
        # Updates existing record state.
        subject = Subject.objects.filter(id=subject_id).first()
        if not subject:
            raise ValueError('Subject record not found')
        
        course = Course.objects.filter(id=course_id).first()
        if not course:
            raise ValueError('Target Course not found')
        
        teacher = Teacher.objects.filter(id=teacher_id).first()
        if not teacher:
            raise ValueError('error' ,'Teacher not found')
        
        subject.name = name
        subject.start_time = start_time
        subject.end_time = end_time
        subject.course = course
        subject.teacher=teacher
        
        subject.save()
        
        return subject
    
    @staticmethod
    def delete_subject(subject_id):
        """
        Deactivates a subject only if it is currently active.
        Prevents redundant database write operations.
        """
        subject = Subject.objects.filter(id=subject_id).first()
        if not subject:
            raise ValueError('Subject record not found')
        
        # Logical check: Only deactivate if the record is currently active
        if subject.is_active:
            subject.is_active = False
            subject.save()
            
        return subject

    @staticmethod
    def recover_subject(subject_id):
        """
        Reactivates a subject only if it is currently inactive (False).
        If already active, the operation is skipped to maintain data consistency.
        """
        subject = Subject.objects.filter(id=subject_id).first()
        if not subject:
            raise ValueError('Subject record not found')
        
        # Logical check: Only reactivate if state is explicitly False
        if subject.is_active == False:
            subject.is_active = True
            subject.save()
            
        return subject