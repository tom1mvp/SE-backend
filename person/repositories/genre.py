from person.models import Genre


class GenreRepository:
    """
    Genre Management Repository

    Handles all persistence logic for gender and identity classifications.
    Provides standardized data for personal records within the school system,
    ensuring consistency in demographic reporting.

    Methods:
    - GET:
        * List all registered genres.
        * Retrieve a specific genre by ID (Primary Key).
        * Search for a genre by its name/description.
    """

    @staticmethod
    def get_all_genre():
        # Retrieve the complete list of genres from the database.
        return Genre.objects.all()
    
    @staticmethod
    def get_genre_by_id(genre_id):
        # Fetch a single genre record using its unique identifier.
        return Genre.objects.filter(id=genre_id).first()
    
    @staticmethod
    def get_genre_by_name(genre_name):
        # Find a genre based on name matches for form selection or filtering.
        return Genre.objects.filter(name__icontains=genre_name).first()