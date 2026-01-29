from rest_framework.validators import ValidationError
from relationship.repositories.relationship import RelationshipRepository

class RelationshipServices:
    """
    Service layer for Relationship management.
    Handles business logic, data validation, and connects API views 
    with the Relationship Repository.
    """

    @staticmethod
    def get_all_relationship():
        # Retrieves all registered relationships through the repository.
        return RelationshipRepository.get_all_relationship()
    
    @staticmethod
    def get_relationship_by_kinship(kinship):
        # Filters relationships based on the kinship type (e.g., Father, Mother).
        return RelationshipRepository.get_relationship_by_kinship(kinship)
    
    @staticmethod
    def get_relationship_by_tutor(name):
        # Business logic to retrieve a relationship record by the tutor's name.
        return RelationshipRepository.get_relationship_by_tutor(name)
    
    @staticmethod
    def create_relationship(
        data,
        tutor_id,
        student_id,
    ):
        """
        Coordinates the creation of a Student-Tutor relationship.
        Validates the presence of mandatory fields before persistence.
        """
        # List of required fields for relationship creation.
        required_fields = ['kinship', 'description']
        
        # Data Integrity Check: Ensure all fields are present in the payload.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        # Invokes repository to create and return the new relationship.
        new_relationship = RelationshipRepository.create_relationship(
            kinship=data['kinship'],
            description=data['description'],
            tutor_id=tutor_id,
            student_id=student_id
        )
        
        return new_relationship
    
    @staticmethod
    def update_relationship(
        data,
        relationship_id,
        tutor_id,
        student_id
    ):
        """
        Coordinates the update process for an existing relationship.
        Re-validates mandatory fields to ensure data consistency.
        """
        # List of required fields for relationship update.
        required_fields = ['kinship', 'description']
        
        # Data Integrity Check: Ensure all fields are present in the payload.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        # Invokes repository to update the record and returns the result.
        relationship = RelationshipRepository.update_relationship(
            relationship_id=relationship_id,
            kinship=data['kinship'],
            description=data['description'],
            tutor_id=tutor_id,
            student_id=student_id
        )

        return relationship # Added return for data flow consistency
        
    @staticmethod
    def delete_relationship(relationship_id):
        # Triggers the logical deletion process via the repository.
        return RelationshipRepository.delete_relationship(relationship_id)
    
    @staticmethod
    def recover_relationship(relationship_id):
        # Reactivates a previously soft-deleted relationship.
        return RelationshipRepository.recover_relationship(relationship_id)