"""
Person Management Service

Acts as the intermediary business logic layer for personal records. 
This service orchestrates data flow between the API views and the PersonRepository, 
ensuring that all operations related to students, staff, and guardians adhere 
to the school's administrative rules and data integrity standards.

Business Logic Handled:
- Unified Data Access: Centralizes retrieval of person profiles.
- Relational Orchestration: Manages complex creation and update processes involving 
  multiple foreign key dependencies (User, Genre, Document, Status, City).
- Lifecycle Control: Executes logical deletion and profile recovery.
"""

from rest_framework.validators import ValidationError


from person.repositories.person import PersonRepository



class PersonServices:
    
    @staticmethod
    def get_all_person():
        # Business logic to retrieve the global list of people in the system.
        return PersonRepository.get_all_person()
    
    @staticmethod
    def get_person_by_id(person_id):
        # Fetches a specific individual's profile by their unique primary key.
        return PersonRepository.get_person_by_id(person_id)
    
    @staticmethod
    def get_person_by_name(first_name):
        # Filters the directory based on partial name matches for administrative search.
        return PersonRepository.get_person_by_name(first_name)
    
    @staticmethod
    def get_person_by_user(user_id):
        # Resolves the connection between a system account and its personal profile.
        return PersonRepository.get_person_by_user(user_id)
    
    @staticmethod
    def create_person(
        data,
        user_id,
        genre_id,
        marital_status_id,
        identity_document_id,
        city_id
    ):
        
        required_fields = [
            'first_name',
            'last_name',
            'mail',
            'number_document',
            'date_of_birth',
            'phone'
            ]
        
        # Verify that all required fields in the form have been filled in.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
        
        # Coordinates the creation of a new person record with validated relations.
        new_person = PersonRepository.create_person(
            first_name=data['first_name'],
            last_name=data['last_name'],
            mail=data['mail'],
            number_document=data['number_document'],
            date_of_birth=data['date_of_birth'],
            phone=data['phone'],
            user_id=user_id,
            genre_id=genre_id,
            marital_status_id=marital_status_id,
            identity_document_id=identity_document_id,
            city_id=city_id
        )
        return new_person
    
    @staticmethod
    def update_person(
        data,
        person_id,
        user_id,
        genre_id,
        marital_status_id,
        identity_document_id,
        city_id
    ):
        # Handles logic for updating personal information and re-validating relationships.
        person = PersonRepository.update_person(
            person_id=person_id,
            first_name=data['first_name'],
            last_name=data['last_name'],
            mail=data['mail'],
            number_document=data['number_document'],
            date_of_birth=data['date_of_birth'],
            phone=data['phone'],
            user_id=user_id,
            genre_id=genre_id,
            marital_status_id=marital_status_id,
            identity_document_id=identity_document_id,
            city_id=city_id
        )
        return person
    
    @staticmethod
    def delete_person(person_id):
        # Triggers logical deletion to archive a profile without erasing data history.
        return PersonRepository.delete_person(person_id)
    
    @staticmethod
    def recover_person(person_id):
        # Restores an archived profile to active status within the institution.
        return PersonRepository.recover_person(person_id)