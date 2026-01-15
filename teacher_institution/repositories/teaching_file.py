from teacher_institution.models import TeachingFile


class TeachingFileRepository:
    """
    Repository class for managing TeachingFile entities (Teacher Professional Records).
    This layer handles the persistence logic for administrative data such as 
    file numbers, professional licenses, and admission dates.
    """

    @staticmethod
    def get_all_teaching_file():
        """
        Retrieves all professional teaching files from the database.
        Typically used for institutional audits or full staff listings.
        """
        return TeachingFile.objects.all()
    
    @staticmethod
    def get_teaching_file_by_id(teaching_file_id):
        """
        Finds a specific professional file by its unique internal database ID.
        """
        return TeachingFile.objects.filter(id=teaching_file_id).first()
    
    @staticmethod
    def get_teaching_file_by_number(number):
        """
        Retrieves a file record based on the public-facing File Number.
        This is the primary method for lookup in administrative workflows.
        """
        return TeachingFile.objects.filter(number=number).first()
    
    @staticmethod
    def create_teaching_file(
        number,
        license_number,
        date_admission
    ):
        """
        Creates and persists a new teacher professional record.
        This record serves as the administrative foundation for a teacher's 
        employment within the institution.
        """
        new_teaching_file = TeachingFile.objects.create(
            number=number,
            license_number=license_number,
            date_admission=date_admission
        )
        
        return new_teaching_file
    
    @staticmethod
    def update_teaching_file(
        teaching_file_id,
        number,
        license_number,
        date_admission
    ):
        """
        Updates the details of an existing professional record.
        It ensures that modifications to the license or admission date 
        are correctly saved to the persistent storage.
        """
        # Locating the existing record for modification
        file = TeachingFile.objects.filter(id=teaching_file_id).first()
        
        if not file:
            raise ValueError('Error', 'File not found')
        
        # Updating record attributes
        file.number = number
        file.license_number = license_number
        file.date_admission = date_admission
        
        # Committing changes to the database
        file.save()
        
        return file