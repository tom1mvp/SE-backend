from rest_framework.validators import ValidationError
from academic.repositories.course import CourseRepository

class CourseServices:
    """
    Service layer for managing Course business logic.
    Acts as a mediator between the API views and the Repository, 
    handling data validation and integrity checks.
    """

    @staticmethod
    def get_all_course():
        # Fetches all existing courses from the database.
        return CourseRepository.get_all_course()
    
    @staticmethod
    def get_course_by_name(name):
        # Business logic for retrieving courses based on a name search.
        return CourseRepository.get_course_by_name(name)
    
    @staticmethod
    def get_course_by_institution(name):
        # Business logic for retrieving courses based on the institution's name.
        return CourseRepository.get_course_by_institution(name)
    
    @staticmethod
    def create_course(data, institution_id):
        """
        Coordinates the creation of a new course record.
        Includes mandatory field verification before persistence.
        """
        # List of essential attributes required to define a course.
        required_fields = ['name', 'section', 'time_slot']
        
        # Data Integrity Check: Verify that all required fields are present in the request payload.
        for field in required_fields:
            if field not in data:
                # Raises a standardized validation error if a mandatory field is missing.
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        # Call the repository to save the validated data.
        new_course = CourseRepository.create_course(
            name=data['name'],
            section=data['section'],
            time_slot=data['time_slot'],
            institution_id=institution_id
        )
        
        return new_course
    
    @staticmethod
    def update_course(data, course_id, institution_id):
        """
        Coordinates the update of an existing course.
        Ensures the payload contains all necessary information for the update.
        """
        # List of essential attributes required for updating a course record.
        required_fields = ['name', 'section', 'time_slot']
        
        # Data Integrity Check: Verify that all required fields are present in the request payload.
        for field in required_fields:
            if field not in data:
                # Raises a standardized validation error if a mandatory field is missing.
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        # Call the repository to update the existing record.
        course = CourseRepository.update_course(
            course_id=course_id,
            name=data['name'],
            section=data['section'],
            time_slot=data['time_slot'],
            institution_id=institution_id
        )
        
        return course