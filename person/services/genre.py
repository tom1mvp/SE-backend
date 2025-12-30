from person.repositories.genre import GenreRepository


class GenreServices:
    """
    Genre Management Service

    Acts as the business logic layer for gender classifications.
    Mediates between the API views and the GenreRepository to ensure 
    standardized data delivery for personal and academic records.

    Business Logic Handled:
    - Data Retrieval: Fetches gender categories for form selection.
    - Identity Validation: Ensures requested genres exist within the system.
    """
    
    @staticmethod
    def get_all_genre():
        # Returns all gender classifications available in the database.
        return GenreRepository.get_all_genre()
    
    @staticmethod
    def get_genre_by_id(genre_id):
        # Retrieves a specific gender record by its primary key.
        return GenreRepository.get_genre_by_id(genre_id)
    
    @staticmethod
    def get_genre_by_name(genre_name):
        # Business logic for searching genres by name or partial string.
        return GenreRepository.get_genre_by_name(genre_name)