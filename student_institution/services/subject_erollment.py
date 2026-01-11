from student_institution.repositories.subject_enrollment import SubjectEnrollmentRepository

class SubjectEnrollmentServices:
    """
    Service layer for SubjectEnrollment.
    Orchestrates business operations related to student subject registrations.
    """

    @staticmethod
    def get_all_subject_enrollment():
        """Fetches all enrollment records by calling the repository layer."""
        return SubjectEnrollmentRepository.get_all_subject_enrollment()
    
    @staticmethod
    def get_subject_enrollment_by_id(subject_enrollment_id):
        """Retrieves a specific enrollment record based on its unique ID."""
        return SubjectEnrollmentRepository.get_subject_enrollment_by_id(subject_enrollment_id)
    
    @staticmethod
    def get_subject_enrollment_by_elective_cycle(elective_cycle_year):
        """Retrieves enrollment data filtered by a specific elective cycle."""
        return SubjectEnrollmentRepository.get_subject_enrollment_by_elective_cycle(elective_cycle_year)
    
    @staticmethod
    def create_subject_enrollment(
        student_id,
        subject_id,
        elective_cycle_id  
    ):
        """
        Logic for enrolling a student in a subject for a specific cycle.
        Interacts with the repository to validate and persist the new record.
        """
        new_subject_enrollment = SubjectEnrollmentRepository.create_subject_enrollment(
            student_id=student_id,
            subject_id=subject_id,
            elective_cycle_id=elective_cycle_id
        )
        
        return new_subject_enrollment
    
    @staticmethod
    def update_subject_enrollment(
        subject_enrollment_id,
        student_id,
        subject_id,
        elective_cycle_id
    ):
        """
        Updates an existing enrollment record.
        Ensures all relational IDs are processed correctly through the repository.
        """
        subject_enrollment = SubjectEnrollmentRepository.update_subject_enrollment(
            subject_enrollment_id=subject_enrollment_id,
            student_id=student_id,
            subject_id=subject_id,
            elective_cycle_id=elective_cycle_id
        )
        
        return subject_enrollment