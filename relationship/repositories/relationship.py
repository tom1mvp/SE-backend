from relationship.models import Relationship
from tutor_institution.models import Tutor
from student_institution.models import Student

class RelationshipRepository:
    """
    Repository layer for Relationship entity.
    Handles direct database interactions (CRUD) using Django ORM.
    """

    @staticmethod
    def get_all_relationship():
        # Retrieves all kinship records stored in the database.
        return Relationship.objects.all()
    
    @staticmethod
    def get_relationship_by_kinship(kinship):
        # Filters relationships based on kinship type using partial matching.
        return Relationship.objects.filter(kinship__icontains=kinship)
    
    @staticmethod
    def get_relationship_by_tutor(name):
        # Retrieves a single relationship record by filtering tutor's first name.
        return Relationship.objects.filter(tutor__person__first_name__icontains=name).first()
    
    @staticmethod
    def create_relationship(
        kinship,
        description,
        tutor_id,
        student_id,
        is_active=True
    ):
        """
        Creates and persists a new Relationship instance.
        Verifies existence of both Tutor and Student entities before creation.
        """
        tutor = Tutor.objects.filter(id=tutor_id).first()
        
        if not tutor:
            raise ValueError('Tutor not found')
        
        student = Student.objects.filter(id=student_id).first()
        
        if not student:
            raise ValueError('Student not found')
        
        new_relationship = Relationship.objects.create(
            kinship=kinship,
            description=description,
            is_active=is_active,
            tutor=tutor,
            student=student
        )
        
        return new_relationship
    
    @staticmethod
    def update_relationship(
        relationship_id,
        kinship,
        description,
        tutor_id,
        student_id,
    ):
        """
        Updates an existing Relationship record.
        Performs lookups for all related entities to ensure referential integrity.
        """
        relationship = Relationship.objects.filter(id=relationship_id).first()
        
        if not relationship:
            raise ValueError('Relationship not found')
        
        tutor = Tutor.objects.filter(id=tutor_id).first()
        
        if not tutor:
            raise ValueError('Tutor not found')
        
        student = Student.objects.filter(id=student_id).first()
        
        if not student:
            raise ValueError('Student not found')
        
        # Mapping updated values to the instance
        relationship.kinship = kinship
        relationship.description = description
        relationship.tutor = tutor
        relationship.student = student
        
        relationship.save()
        
        return relationship
    
    @staticmethod
    def delete_relationship(relationship_id):
        """
        Performs a logical delete by deactivating the relationship record.
        """
        relationship = Relationship.objects.filter(id=relationship_id).first()
        
        if not relationship:
            raise ValueError('Relationship not found')
        
        if relationship.is_active:
            relationship.is_active = False
            relationship.save()
            
        return relationship
    
    @staticmethod
    def recover_relationship(relationship_id):
        """
        Reactivates a previously deactivated relationship record.
        """
        relationship = Relationship.objects.filter(id=relationship_id).first()
        
        if not relationship:
            raise ValueError('Relationship not found')
        
        if not relationship.is_active:
            relationship.is_active = True
            relationship.save()
            
        return relationship