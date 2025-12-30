from person.repositories.identity_document import IdentityDocumentRepository


class IdentityDocumentServices:
    """
    Identity Document Management Service

    Orchestrates business logic for legal identification types.
    Acts as a mediator between the API controllers and the IdentityDocumentRepository,
    ensuring that the school system handles student and staff IDs under valid 
    legal frameworks.

    Business Logic Handled:
    - Document Validation: Centralizes the logic for retrieving valid ID types.
    - Enrollment Support: Provides the necessary document categories for new student registration.
    """
    
    @staticmethod
    def get_all_identity_document():
        # Retrieves all legal identification categories supported by the institution.
        return IdentityDocumentRepository.get_all_identity_document()
    
    @staticmethod
    def get_identity_document_by_id(document_id):
        # Business logic to fetch a specific identity document type by its ID.
        return IdentityDocumentRepository.get_identity_document_by_id(document_id)
    
    @staticmethod
    def get_identity_document_by_name(document_name):
        # Filters identity documents by name or acronym (e.g., DNI, PAS, CPI).
        return IdentityDocumentRepository.get_identity_document_by_name(document_name)