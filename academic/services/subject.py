"""
SUBJECT SERVICE LAYER - ARCHITECTURAL OVERVIEW:
This module acts as the intermediary between the View Layer and the Data Access Layer (Repository).
The Service Layer is responsible for orchestrating business logic and ensuring data flows correctly.

KEY RESPONSIBILITIES:
1. BUSINESS LOGIC: Processing and transforming data before it reaches the repository or the view.
2. ABSTRACTION: The View doesn't need to know how the database works; it only talks to this Service.
3. DATA ORCHESTRATION: Extracting specific fields from request dictionaries and passing them 
   as clean arguments to the Repository methods.

By separating this layer, we ensure that if we ever change how a subject is created 
(e.g., adding an email notification), we only change it here, not in the View or the Repository.
"""

from academic.repositories.subject import SubjectRepository

class SubjectServices:
    @staticmethod
    def get_all_subject():
        """Logic to retrieve all subjects through the repository."""
        return SubjectRepository.get_all_subject()

    @staticmethod
    def get_subject_by_id(subject_id):
        """Logic to fetch a specific subject by ID."""
        return SubjectRepository.get_subject_by_id(subject_id)

    @staticmethod
    def get_subject_name(name):
        """Logic to search subjects by their name."""
        return SubjectRepository.get_subject_by_name(name)

    @staticmethod
    def create_subject(data, institution_id):
        """
        Orchestrates the creation process.
        Extracts raw data from the 'data' dictionary and passes clean variables to the repository.
        """
        return SubjectRepository.create_subject(
            name=data['name'],
            section=data['section'],
            time_slot=data['time_slot'],
            institution_id=institution_id
        )

    @staticmethod
    def update_subject(data, subject_id, institution_id):
        """
        Orchestrates the update process.
        Ensures the service handles the mapping between request data and repository parameters.
        """
        return SubjectRepository.update_subject(
            subject_id=subject_id,
            name=data['name'],
            section=data['section'],
            time_slot=data['time_slot'],
            institution_id=institution_id
        )