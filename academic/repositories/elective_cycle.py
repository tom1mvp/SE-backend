"""
Elective Cycle Management Repository

Handles the persistence logic for academic periods. This module is the 
chronological heart of the school system, defining the start and end 
boundaries for enrollments, attendance, and grading periods.

Methods:
- POST:
    * Create new elective cycles (e.g., Year 2026).
- PATCH:
    * Logical deactivation of academic periods to finalize school years.
"""

from academic.models import ElectiveCycle


class ElectiveCycleRepository:
    
    @staticmethod
    def get_elective_cycle_by_end_date(elective_cycle_end_date):
        return ElectiveCycle.objects.filter(end_date=elective_cycle_end_date).first()
    
    @staticmethod
    def create_elective_cycle(
      year,
      start_date,
      end_date,
      is_active=True
    ):
        # Register a new academic year within the institutional calendar.
        new_elective_cycle = ElectiveCycle.objects.create(
            year=year,
            start_date=start_date,
            end_date=end_date,
            is_active=is_active
        )
        
        return new_elective_cycle
    
    @staticmethod
    def disable_elective_cycle(elective_cycle_id):
        # Locate the specific academic period by its ID.
        elective_cycle = ElectiveCycle.objects.filter(id=elective_cycle_id).first()
        
        if not elective_cycle:
            raise ValueError('Error', 'Elective cycle not found')
        
        # Perform a logical shutdown of the cycle to prevent further academic changes.
        if elective_cycle.is_active:
            elective_cycle.is_active = False
            
            elective_cycle.save()
            
            return elective_cycle