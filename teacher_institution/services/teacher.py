from rest_framework.validators import ValidationError
from teacher_institution.repositories.teacher import TeacherRepository


class TeacherServices:
    """
    Service layer for Teacher management.
    This class acts as a coordinator between the API layer and the Repository,
    handling the business logic required to link personal identities with 
    professional records.
    """

    @staticmethod
    def get_all_teacher():
        """
        Retrieves a complete list of all teachers in the institution 
        through the repository.
        """
        return TeacherRepository.get_all_teacher()
    
    @staticmethod
    def get_teacher_by_id(teacher_id):
        """
        Retrieves a specific teacher profile using its primary key.
        """
        return TeacherRepository.get_teacher_by_id(teacher_id)
    
    @staticmethod
    def get_teacher_by_name(name):
        """
        Searches for a teacher profile based on the name stored in the 
        linked Person record.
        """
        return TeacherRepository.get_teacher_by_name(name)
    
    @staticmethod
    def create_teacher(data, person_id, file_id):
        """
        Coordinates the creation of a new Teacher profile.
        It links a pre-existing Person record and a TeachingFile record 
        to form a complete institutional profile.
        """
        # Execution of the creation logic via the repository
        new_teacher = TeacherRepository.create_teacher(
            person_id=person_id,
            file_id=file_id
        )
        
        return new_teacher