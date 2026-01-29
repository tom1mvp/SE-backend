from academic.models import Course
from establishment.models import Institution


class CourseRepository:
    """
    Repository class for Course model.
    Handles all database operations related to courses, ensuring data persistence 
    and retrieval logic is separated from business rules.
    """

    @staticmethod
    def get_all_course():
        # Retrieves all course records from the database.
        return Course.objects.all()
    
    @staticmethod
    def get_course_by_name(name):
        # Filters courses where the name contains the provided string (case-insensitive).
        return Course.objects.filter(name__icontains=name)
    
    @staticmethod
    def get_course_by_institution(name):
        # Retrieves courses belonging to an institution based on the institution's name.
        return Course.objects.filter(institution__name__icontains=name)
    
    @staticmethod
    def create_course(name, section, time_slot, institution_id):
        """
        Creates and saves a new Course instance.
        Validates institution existence before assignment.
        """
        institution = Institution.objects.filter(id=institution_id).first()
        
        if not institution:
            raise ValueError('Institution not found')
        
        new_course = Course.objects.create(
            name=name,
            section=section,
            time_slot=time_slot,
            institution=institution
        )
        
        return new_course
    
    @staticmethod
    def update_course(course_id, name, section, time_slot, institution_id):
        """
        Updates an existing course record.
        Ensures both the course and the target institution exist.
        """
        course = Course.objects.filter(id=course_id).first()
        
        if not course:
            raise ValueError('Course not found')
        
        institution = Institution.objects.filter(id=institution_id).first()
        
        if not institution:
            raise ValueError('Institution not found')
        
        course.name = name
        course.section = section
        course.time_slot = time_slot
        course.institution = institution
        
        course.save()
        return course