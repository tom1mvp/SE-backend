from person.models import IdentityDocument


class IdentityDocumentRepository:
    """
    Identity Document Management Repository

    Handles the persistence logic for various types of legal identifications. 
    Crucial for student enrollment and formal record-keeping, ensuring each 
    individual is registered under a valid legal framework.

    Methods:
    - GET:
        * List all supported identity document types.
        * Retrieve a specific document type by ID (Primary Key).
        * Search for document types by name or acronym (e.g., DNI, PAS).
    """

    @staticmethod
    def get_all_identity_document():
        # Retrieve all legal document classifications available in the system.
        return IdentityDocument.objects.all()
    
    @staticmethod
    def get_identity_document_by_id(document_id):
        # Fetch a specific document classification using its unique identifier.
        return IdentityDocument.objects.filter(id=document_id).first()
    
    @staticmethod
    def get_identity_document_by_name(document_name):
        # Resolve document types by their name or abbreviation for validation logic.
        # Returns a QuerySet for flexible matching.
        return IdentityDocument.objects.filter(name__icontains=document_name).first()