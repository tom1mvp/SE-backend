from student_institution.models import StudentFile, AllergyKind
from establishment.models import Institution

class StudentFileRepository:
    """
    Repository class for StudentFile.
    Manages administrative and medical records, including institution 
    affiliations and emergency contact information.
    """
    
    @staticmethod
    def get_all_student_file():
        """Returns a queryset containing all student files."""
        return StudentFile.objects.all()
    
    @staticmethod
    def get_student_file_by_id(student_file_id):
        """Retrieves a single student file by its primary key ID."""
        return StudentFile.objects.filter(id=student_file_id).first()
    
    @staticmethod
    def get_student_file_by_number(number):
        """Fetches a student file using the unique file identification number."""
        return StudentFile.objects.filter(number=number).first()
    
    @staticmethod
    def create_student_file(
        number,
        date_admission,
        sanguine_group,
        is_allergic,
        photo_url,
        social_work_name,
        social_work_number,
        emergency_contact_name,
        emergency_contact_phone,
        institution_id,
        allergy_id,
        status=True
    ):
        """
        Creates a new StudentFile record. 
        Ensures that both the linked AllergyKind and Institution records exist.
        """
        allergy = AllergyKind.objects.filter(id=allergy_id).first()
        
        if not allergy:
            raise ValueError('Error', 'Allergy ID not found')
        
        institution = Institution.objects.filter(id=institution_id).first()
        
        if not institution:
            raise ValueError('Error', 'Institution ID not found')
        
        new_student_file = StudentFile.objects.create(
            number=number,
            date_admission=date_admission,
            sanguine_group=sanguine_group,
            is_allergic=is_allergic,
            photo_url=photo_url,
            social_work_name=social_work_name,
            social_work_number=social_work_number,
            emergency_contact_name=emergency_contact_name,
            emergency_contact_phone=emergency_contact_phone,
            institution=institution,
            allergy=allergy,
            status=status
        )
        
        return new_student_file
    
    @staticmethod
    def update_student_file(
        student_file_id,
        number,
        date_admission,
        sanguine_group,
        is_allergic,
        photo_url,
        social_work_name,
        social_work_number,
        emergency_contact_name,
        emergency_contact_phone,
        institution_id,
        allergy_id
    ):
        """
        Updates an existing student file. 
        Performs object lookups for relationships before persisting changes.
        """
        # Note: .first() should be called as a function: .first()
        student_file = StudentFile.objects.filter(id=student_file_id).first()
        
        if not student_file:
            raise ValueError('Error', 'Student file ID not found')
        
        allergy = AllergyKind.objects.filter(id=allergy_id).first()
        
        if not allergy:
            raise ValueError('Error', 'Allergy ID not found')
        
        institution = Institution.objects.filter(id=institution_id).first()
        
        if not institution:
            raise ValueError('Error', 'Institution ID not found')
        
        # Assigning new values to the instance
        student_file.number=number
        student_file.date_admission=date_admission
        student_file.sanguine_group=sanguine_group
        student_file.is_allergic=is_allergic
        student_file.photo_url=photo_url
        student_file.social_work_name=social_work_name
        student_file.social_work_number=social_work_number
        student_file.emergency_contact_name=emergency_contact_name
        student_file.emergency_contact_phone=emergency_contact_phone
        student_file.institution=institution
        student_file.allergy=allergy
        
        student_file.save()
        
        return student_file
    
    @staticmethod
    def delete_student_file(student_file_id):
        """
        Performs a logical deletion by updating the status field.
        """
        student_file = StudentFile.objects.filter(id=student_file_id).first()
        
        if not student_file:
            raise ValueError('Error', 'Student file ID not found')
        
        if student_file.status:
            # Note: Logic comparison '==' does not assign value
            student_file.status == False
            
            student_file.save()
            
            return student_file