"""
Person Management Repository

This repository centralizes all persistence logic for personal data within the school system.
It manages the complete lifecycle of individuals—including students, teachers, and guardians—
ensuring data integrity through strict validation of foreign key relationships (User, Genre, 
IdentityDocument, MaritalStatus, and City).

Methods:
- GET: 
    * List all persons.
    * Search by primary key, associated user, or first name (partial match).
- POST: Create a new person profile with validated demographic and geographic links.
- PUT: Update existing personal information and relational data.
- PATCH:
    * Soft delete by deactivating the person's profile status.
    * Recovery of inactive profiles to restore system access.
"""

from person.models import (
        Person,
        Genre,
        IdentityDocument,
        MaritalStatus
    )
from user.models import User
from region.models import City


class PersonRepository:
    
    @staticmethod
    def get_all_person():
        # Retrieve all personal records from the database.
        return Person.objects.all()
    
    @staticmethod
    def get_person_by_id(person_id):
        # Fetch a single person record by their primary key.
        return Person.objects.filter(id=person_id).first()
    
    @staticmethod
    def get_person_by_name(first_name):
        # Filter persons by a partial match of their first name.
        return Person.objects.filter(first_name__icontains=first_name)
    
    @staticmethod
    def get_person_by_user(user_id):
        # Find the specific person profile associated with a User account.
        return Person.objects.filter(user_id=user_id).first()
    
    @staticmethod
    def create_person(
        first_name,
        last_name,
        mail,
        number_document,
        date_of_birth,
        phone,
        user_id,
        genre_id,
        marital_status_id,
        identity_document_id,
        city_id,
        is_active=True,
    ):
        # Verify that all mandatory relational entities exist before creation.
        user = User.objects.filter(id=user_id).first()
        if not user: raise ValueError('User not found')
        
        genre = Genre.objects.filter(id=genre_id).first()
        if not genre: raise ValueError('Genre not found')
        
        marital_status = MaritalStatus.objects.filter(id=marital_status_id).first()
        if not marital_status: raise ValueError('Marital status not found')
        
        identity_document = IdentityDocument.objects.filter(id=identity_document_id).first()
        if not identity_document: raise ValueError('Identity document not found')
        
        city = City.objects.filter(id=city_id).first()
        if not city: raise ValueError('City not found')
        
        # Persist the new person record with its validated relationships.
        new_person = Person.objects.create(
            first_name=first_name,
            last_name=last_name,
            mail=mail,
            number_document=number_document,
            date_of_birth=date_of_birth,
            phone=phone,
            user=user,
            genre=genre,
            marital_status=marital_status,
            identity_document=identity_document,
            city=city,
            is_active=is_active
        )
        return new_person
    
    @staticmethod
    def update_person(
        person_id,
        first_name,
        last_name,
        mail,
        number_document,
        date_of_birth,
        phone,
        user_id,
        genre_id,
        marital_status_id,
        identity_document_id,
        city_id,
    ):
        # Locate the existing record and validate new relationship assignments.
        person = Person.objects.filter(id=person_id).first()
        if not person:
            raise ValueError('Person not found')
        
        user = User.objects.filter(id=user_id).first()
        genre = Genre.objects.filter(id=genre_id).first()
        marital_status = MaritalStatus.objects.filter(id=marital_status_id).first()
        identity_document = IdentityDocument.objects.filter(id=identity_document_id).first()
        city = City.objects.filter(id=city_id).first()
        
        # Apply updates to the person instance fields.
        person.first_name = first_name
        person.last_name = last_name
        person.mail = mail
        person.number_document = number_document
        person.date_of_birth = date_of_birth
        person.phone = phone
        person.user = user
        person.genre = genre
        person.marital_status = marital_status
        person.identity_document = identity_document
        person.city = city
        
        person.save()
        return person
    
    @staticmethod
    def delete_person(person_id):
        # Perform a logical delete by setting is_active to False.
        person = Person.objects.filter(id=person_id).first()
        if not person: raise ValueError('Person not found')
        
        if person.is_active:
            person.is_active = False
            person.save()
        return person

    @staticmethod
    def recover_person(person_id):
        # Restore a previously deactivated person profile.
        person = Person.objects.filter(id=person_id).first()
        if not person: raise ValueError('Person not found')
        
        if not person.is_active:
            person.is_active = True
            person.save()
        return person