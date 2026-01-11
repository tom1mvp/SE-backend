from rest_framework.validators import ValidationError


from student_institution.repositories.student import StudentRepository

class StudentServices:
    """
    Service layer to handle business logic for Student entities.
    It orchestrates the data flow between the view and the repository.
    """

    @staticmethod
    def get_all_student():
        """Fetches all students through the repository layer."""
        return StudentRepository.get_all_student()
    
    @staticmethod
    def get_student_by_id(student_id):
        """Retrieves a single student by ID using the repository."""
        return StudentRepository.get_student_by_id(student_id)
    
    @staticmethod
    def get_student_by_name(student_name):
        """Filters students by name through the repository's search logic."""
        return StudentRepository.get_student_by_name(student_name)
    
    @staticmethod
    def create_student(
      data,
      person_id,
      student_file_id,
    ):
        """
        Triggers the creation of a student record.
        Additional data validation can be implemented here before hitting the repo.
        """
        new_student = StudentRepository.create_student(
            person_id=person_id,
            student_file_id=student_file_id
        )
        
        return new_student
    
    @staticmethod
    def delete_student(
        student_id
    ):
        """Handles the request to perform a logical deletion of a student."""
        return StudentRepository.delete_student(student_id)
    
    @staticmethod
    def recover_student(
        student_id
    ):
        """Handles the request to restore a student from an inactive state."""
        return StudentRepository.recover_student(student_id)