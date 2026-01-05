"""
History Institution Management Repository

This module handles the archival and historical data for educational entities. 
It manages the long-term records of an institution, including its founding 
narrative, original leadership, and multimedia legacy.

Key Responsibilities:
- Historical Retrieval: Accessing the biography and foundation details.
- Data Integrity: Ensuring that each history record is uniquely tied to a valid Institution.
- Content Maintenance: Updating the institutional legacy and founder information.
"""

from establishment.models import HistoryInstitution, Institution


class HistoryInstitutionRepository:
    @staticmethod
    def get_all_history_institution():
        # Retrieves the complete archive of all institutional histories.
        return HistoryInstitution.objects.all()
    
    @staticmethod
    def get_history_institution_by_id(history_institution_id):
        # Fetches a specific historical record by its primary key.
        return HistoryInstitution.objects.filter(id=history_institution_id).first()
    
    @staticmethod
    def get_history_institution_by_institution(institution_id):
        # Retrieves the specific history associated with a given institution ID.
        return HistoryInstitution.objects.filter(institution_id=institution_id).first()
    
    @staticmethod
    def create_history_institution(
      biography,
      foundation_date,
      multimedia_url,
      founder,
      institution_id
    ):
        # Verifies the existence of the institution before creating its history.
        institution = Institution.objects.filter(id=institution_id).first()
        
        if not institution:
            raise ValueError('Error', 'Institution not found')
        
        # Persists the foundational data and biographical narrative.
        new_history_institution = HistoryInstitution.objects.create(
            biography=biography,
            foundation_date=foundation_date,
            multimedia_url=multimedia_url,
            founder=founder,
            institution=institution
        )
        
        return new_history_institution
    
    @staticmethod
    def update_history_institution(
      history_institution_id,
      biography,
      foundation_date,
      multimedia_url,
      founder,
      institution_id
    ):
        
        # Locates the historical record to be updated.
        history_institution = HistoryInstitution.objects.filter(id=history_institution_id).first()
        
        if not history_institution:
            raise ValueError('Error', 'History institution not found')
        
        # Ensures the linked institution remains valid during the update.
        institution = Institution.objects.filter(id=institution_id).first()
        
        if not institution:
            raise ValueError('Error', 'Institution not found')
        
        # Synchronizes the updated biography and historical facts to the database.
        history_institution.biography=biography
        history_institution.foundation_date=foundation_date
        history_institution.multimedia_url=multimedia_url
        history_institution.founder=founder
        history_institution.institution=institution
        
        history_institution.save()
        
        return history_institution