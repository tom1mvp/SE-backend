from tutor_institution.models import Tutor
from person.models import Person


class TutorRepository:
    """
    Repository class to handle data access logic for the Tutor model.
    This layer centralizes all database queries related to tutors, acting as 
    an abstraction between the business logic and the Django ORM. It ensures 
    that the rest of the application interacts with a clean API for tutor data.
    """

    @staticmethod
    def get_all_tutor():
        """
        Retrieves all tutor records currently stored in the database.
        This provides a complete collection of tutors for general administrative 
        views or institutional lists.
        """
        return Tutor.objects.all()
    
    @staticmethod
    def get_tutor_by_id(tutor_id):
        """
        Fetches a single tutor instance based on its primary key (ID).
        Utilizing .filter().first() ensures that the application returns None 
        if the record does not exist, rather than raising a system-wide exception.
        """
        return Tutor.objects.filter(id=tutor_id).first()
    
    @staticmethod
    def get_tutor_by_relationship(relationship):
        """
        Filters the tutor database based on the specific legal or personal 
        relationship with the student (e.g., 'Mother', 'Legal Guardian').
        This is useful for categorization and emergency contact sorting.
        """
        return Tutor.objects.filter(relationship__icontains=relationship)
    
    @staticmethod
    def get_tutor_by_name(name):
        """
        Searches for tutors by performing a join-like operation with the Person model.
        It uses the double underscore (__icontains) to look into the related 
        Person entity's first name, allowing for case-insensitive partial matches.
        """
        return Tutor.objects.filter(person__first_name__icontains=name)
    
    @staticmethod
    def create_tutor(
        person_id,
        relationship
    ):
        """
        Executes the creation of a new Tutor record after validating dependencies.
        It first verifies that the designated Person exists to maintain 
        referential integrity, then instantiates the Tutor with the provided 
        relationship details.
        """
        # Verification of the Person entity to prevent Foreign Key errors
        person = Person.objects.filter(id=person_id).first()
        
        if not person:
            # Raising a controlled error to be caught by the service or controller layers
            raise ValueError('Error', 'Person not found')
        
        # Persistence of the new tutor record
        new_tutor = Tutor.objects.create(
            relationship=relationship,
            person=person
        )
        
        return new_tutor