from student_institution.models import SubjectEnrollment, Student
from academic.models import ElectiveCycle, Subject

class SubjectEnrollmentRepository:
    """
    Repository class for SubjectEnrollment.
    Handles the persistence logic for student enrollments in specific subjects
    during a given elective cycle.
    """

    @staticmethod
    def get_all_subject_enrollment():
        """Retrieves all enrollment records from the database."""
        return SubjectEnrollment.objects.all()
    
    @staticmethod
    def get_subject_enrollment_by_id(subject_enrollment_id):
        """Finds a specific enrollment record by its unique ID."""
        return SubjectEnrollment.objects.filter(id=subject_enrollment_id).first()
    
    @staticmethod
    def get_subject_enrollment_by_elective_cycle(elective_cycle_year):
        """
        Retrieves enrollment records filtered by a specific elective cycle.
        Note: .first() returns only one record; consider .all() if you need the full list.
        """
        return SubjectEnrollment.objects.filter(elective_cycle__year=elective_cycle_year)
    
    @staticmethod
    def create_subject_enrollment(
        student_id,
        subject_id,
        elective_cycle_id
    ):
        """
        Creates a new enrollment record after validating that the Student,
        Subject, and ElectiveCycle exist.
        """
        # Note: Added 'id=' to the filter for consistency
        student = Student.objects.filter(id=student_id).first()
        
        if not student:
            raise ValueError('Error', 'Student ID not found')
        
        subject = Subject.objects.filter(id=subject_id).first()
        
        if not subject:
            raise ValueError('Error', 'Subject ID not found')
        
        elective_cycle = ElectiveCycle.objects.filter(id=elective_cycle_id).first()
        
        if not elective_cycle:
            raise ValueError('Error', 'Elective Cycle ID not found')
            
        new_subject_enrollment = SubjectEnrollment.objects.create(
            student=student,
            subject=subject,
            elective_cycle=elective_cycle
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
        Updates an existing enrollment. Validates all foreign keys 
        before committing the changes to the database.
        """
        student = Student.objects.filter(id=student_id).first()
        
        if not student:
            raise ValueError('Error', 'Student ID not found')
        
        subject = Subject.objects.filter(id=subject_id).first()
        
        if not subject:
            raise ValueError('Error', 'Subject ID not found')
        
        elective_cycle = ElectiveCycle.objects.filter(id=elective_cycle_id).first()
        
        if not elective_cycle:
            raise ValueError('Error', 'Elective Cycle ID not found')
        
        subject_enrollment = SubjectEnrollment.objects.filter(id=subject_enrollment_id).first()
        
        if not subject_enrollment:
            raise ValueError('Error', 'Subject enrollment ID not found')
        
        # Mapping updated objects to the instance
        subject_enrollment.student = student
        subject_enrollment.subject = subject
        subject_enrollment.elective_cycle = elective_cycle
        
        # Persisting changes
        subject_enrollment.save()
        
        return subject_enrollment