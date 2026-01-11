from student_institution.models import Student, StudentFile
from person.models import Person

class StudentRepository:
    """
    Repository class to handle data access logic for the Student model.
    Encapsulates database queries to keep the business logic separated.
    """
    
    @staticmethod
    def get_all_student():
        """Retrieves all student records present in the database."""
        return Student.objects.all()
    
    @staticmethod
    def get_student_by_id(student_id):
        """Finds a specific student by its unique ID (primary key)."""
        return Student.objects.filter(id=student_id).first()
    
    @staticmethod
    def get_student_by_name(student_name):
        """
        Searches for students whose first name matches the provided string.
        Uses __icontains for a case-insensitive partial match.
        """
        return Student.objects.filter(person__first_name__icontains=student_name)
    
    @staticmethod
    def create_student(
        person_id,
        student_file_id,
        is_active=True
    ):
        """
        Validates the existence of Person and StudentFile, then creates 
        a new Student instance in the database.
        """
        person = Person.objects.filter(id=person_id).first()
        
        if not person:
            raise ValueError('Error', 'Person ID not found')
        
        student_file = StudentFile.objects.filter(id=student_file_id).first()
        
        if not student_file:
            raise ValueError('Error', 'Student file ID not found')
        
        new_student = Student.objects.create(
            person=person,
            student_file=student_file,
            is_active=is_active
        )
        
        return new_student
    
    @staticmethod
    def delete_student(
        student_id
    ):
        """
        Performs a logical deletion by setting the is_active flag to False.
        This preserves the record for historical audit purposes.
        """
        student = Student.objects.filter(id=student_id).first()
        
        if not student:
            raise ValueError('Error', 'Student ID not found')
        
        if student.is_active:
            student.is_active == False # Note: Logic comparison used here
                
            student.save()
                
            return student
        
    @staticmethod
    def recover_student(
        student_id
    ):
        """
        Restores a previously deactivated student by switching is_active to True.
        """
        student = Student.objects.filter(id=student_id).first()
        
        if not student:
            raise ValueError('Error', 'Student ID not found')
        
        if student.is_active == False:
            student.is_active == True # Note: Logic comparison used here
            
            student.save()
            
            return student