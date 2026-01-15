from teacher_institution.models import Teacher, TeachingFile
from person.models import Person


class TeacherRepository:
    """
    Repository class for managing Teacher entities.
    This layer coordinates the relationship between a Person (identity) 
    and a TeachingFile (administrative record), ensuring that the teacher 
    profile is correctly linked and persisted.
    """

    @staticmethod
    def get_all_teacher():
        """
        Retrieves all registered teachers in the system.
        Commonly used to populate staff directories or selection lists.
        """
        return Teacher.objects.all()
    
    @staticmethod
    def get_teacher_by_id(teacher_id):
        """
        Fetches a single teacher instance by its primary key.
        Useful for detailed profile views or individual record management.
        """
        return Teacher.objects.filter(id=teacher_id).first()
    
    @staticmethod
    def get_teacher_by_name(name):
        """
        Locates a teacher based on the first name within the related Person model.
        Uses case-insensitive containment lookup (icontains) through the relationship.
        """
        # Traverses the Person relationship to search by the first_name attribute
        return Teacher.objects.filter(person__first_name__icontains=name).first()
    
    @staticmethod
    def create_teacher(
        person_id,
        file_id
    ):
        """
        Creates a new Teacher profile by linking an existing Person with a TeachingFile.
        Validates both dependencies before creation to ensure structural integrity.
        """
        # Verifying the existence of the physical person identity
        person = Person.objects.filter(id=person_id).first()
        if not person:
            raise ValueError('Error', 'Person not found')
        
        # Verifying the existence of the administrative teaching file
        file = TeachingFile.objects.filter(id=file_id).first()
        if not file:
            raise ValueError('Error', 'File not found')
        
        # Linking both entities into a single Teacher profile
        new_teacher = Teacher.objects.create(
            person=person,
            file=file
        )
        
        return new_teacher