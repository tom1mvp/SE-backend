"""
Elective Cycle Management Service

This service orchestrates the lifecycle of the academic year. It provides 
automated logic to open new school cycles based on the current calendar year 
and manages the automatic transition to inactive status when the institutional 
closing dates are met.

Business Logic:
- Automatic Creation: Sets default start (March 10th) and end (December 20th) dates.
- Automatic Deactivation: Identifies and disables cycles that have reached their conclusion.
"""

import datetime


from datetime import date


from academic.repositories.elective_cycle import ElectiveCycleRepository

class ElectiveCycleServices:
    
    @staticmethod
    def create_elective_cycle():
        # Get the current year from the system clock
        current_year = datetime.date.today().year
        
        # Define the institutional academic boundaries
        start_date = datetime.datetime(current_year, 2, 26)
        end_date = datetime.datetime(current_year, 12, 15)
        
        # Persist the new cycle through the repository
        new_elective_cycle = ElectiveCycleRepository.create_elective_cycle(
            year=current_year,
            start_date=start_date,
            end_date=end_date
        )
        
        return new_elective_cycle
    
    @staticmethod
    def disable_elective_cycle():
        # Reference today's date to check for expired cycles
        today = datetime.date.today()
        
        # Retrieve all cycles that should end on or before today
        elective_cycle_end = ElectiveCycleRepository.get_elective_cycle_by_end_date(today)
        
        if elective_cycle_end:
            # Process each expired cycle found in the repository
            for cycle in elective_cycle_end:
                ElectiveCycleRepository.disable_elective_cycle(cycle.id)
            
            # Return true after processing all identified cycles
            return True
        return False