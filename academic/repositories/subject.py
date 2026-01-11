"""
This module implements the Repository Pattern for the Subject entity. 
The Repository layer is responsible for direct communication with the database via Django's ORM.

KEY ARCHITECTURAL BENEFITS:
1. ENCAPSULATION: It isolates the queries (SQL/ORM logic) from the Service Layer. If the database 
   schema or the ORM changes, only this file needs modification.
2. REUSABILITY: Standardized methods for fetching, creating, and updating Subjects can be called 
   by any service or management command without duplicating logic.
3. DATA INTEGRITY: Centralizes database operations like filtering by ID or checking foreign key 
   existence (Institution) before performing write operations.

Logic Flow:
- Read operations (get_all, get_by_id) return Model instances or QuerySets.
- Write operations (create, update) perform validations on foreign keys to prevent Database Integrity 
  Errors and ensure the 'Subject' is always linked to a valid 'Institution'.
"""

from academic.models import Subject
from establishment.models import Institution


class SubjectRepository:
    @staticmethod
    def get_all_subject():
        """Fetches all subject records from the database."""
        return Subject.objects.all()
    
    @staticmethod
    def get_subject_by_id(subject_id):
        """Retrieves a single subject by its primary key."""
        return Subject.objects.filter(id=subject_id).first()
    
    @staticmethod
    def get_subject_by_name(subject_name):
        """Filters subjects using a case-insensitive partial match on the name."""
        return Subject.objects.filter(name__icontains=subject_name).first()
    
    @staticmethod
    def create_subject(
        name,
        section,
        time_slot,
        institution_id
    ):
        """Validates the institution existence and creates a new Subject record."""
        institution = Institution.objects.filter(id=institution_id).first()
        
        if not institution:
            raise ValueError('Institution not found')
        
        new_subject = Subject.objects.create(
            name=name,
            section=section,
            time_slot=time_slot,
            institution=institution
        )
        
        return new_subject
    
    @staticmethod
    def update_subject(
        subject_id,
        name,
        section,
        time_slot,
        institution_id
    ):
        """Updates an existing Subject record after validating both Subject and Institution presence."""
        subject = Subject.objects.filter(id=subject_id).first()
        
        if not subject:
            raise ValueError('Subject not found')
        
        institution = Institution.objects.filter(id=institution_id).first()
        
        if not institution:
            raise ValueError('Institution not found')
        
        # Mapping updated values to the instance fields
        subject.name = name
        subject.section = section
        subject.time_slot = time_slot
        subject.institution = institution
        
        subject.save()
        
        return subject