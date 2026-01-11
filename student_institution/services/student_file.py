from rest_framework.validators import ValidationError


from student_institution.repositories.student_file import StudentFileRepository


class StudentFileServices:
    """
    Service layer for StudentFile operations.
    Encapsulates the business logic and orchestrates data mapping between 
    the input data (dictionaries) and the repository methods.
    """

    @staticmethod
    def get_all_student_file():
        """Fetches all existing student files from the database."""
        return StudentFileRepository.get_all_student_file()
    
    @staticmethod
    def get_student_file_by_id(student_file_id):
        """Retrieves a single student file using its unique ID."""
        return StudentFileRepository.get_student_file_by_id(student_file_id)
    
    @staticmethod
    def get_student_file_by_number(number):
        """Retrieves a student file based on the administrative file number."""
        return StudentFileRepository.get_student_file_by_number(number)
    
    @staticmethod
    def crear_student_file(
        data,
        institution_id,
        allergy_id
    ):
        """
        Orchestrates the creation of a new student file.
        Maps the dictionary fields from the request to the repository parameters.
        """
        new_student_file = StudentFileRepository.create_student_file(
            number=data['number'],
            date_admission=data['date_admission'],
            sanguine_group=data['sanguine_group'],
            is_allergic=data['is_allergic'],
            photo_url=data['photo_url'],
            social_work_name=data['social_work_name'],
            social_work_number=data['social_work_number'],
            emergency_contact_name=data['emergency_contact_name'],
            emergency_contact_phone=data['emergency_contact_phone'],
            institution_id=institution_id,
            allergy_id=allergy_id
        )
        
        return new_student_file
    
    @staticmethod
    def update_student_file(
        data,
        student_file_id,
        institution_id,
        allergy_id
    ):
        """
        Coordinates the update of an existing student file.
        Extracts values from the data payload to pass them to the repository layer.
        """
        student_file = StudentFileRepository.update_student_file(
            student_file_id=student_file_id,
            number=data['number'],
            date_admission=data['date_admission'],
            sanguine_group=data['sanguine_group'],
            is_allergic=data['is_allergic'],
            photo_url=data['photo_url'],
            social_work_name=data['social_work_name'],
            social_work_number=data['social_work_number'],
            emergency_contact_name=data['emergency_contact_name'],
            emergency_contact_phone=data['emergency_contact_phone'],
            institution_id=institution_id,
            allergy_id=allergy_id
        )
        
        return student_file
    
    @staticmethod
    def delete_student_file(student_file_id):
        """
        Requests the logical deletion of a student file via the repository.
        """
        return StudentFileRepository.delete_student_file(student_file_id)