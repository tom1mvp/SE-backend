import datetime


from django.core.management.base import BaseCommand


from academic.models import ElectiveCycle
from establishment.services.institution import InstitutionServices



class Command(BaseCommand):
    """
    Annual Institutional Cycle Synchronization Command
    
    This command automates the transition of all educational entities to the 
    current academic year. It retrieves the ElectiveCycle corresponding to 
     the current year and updates the reference in every institution record.
    
    Logic:
    - Target: Uses the 'year' field from your ElectiveCycle model.
    - Scope: Iterates through all institutions using your Service layer.
    """
    
    help = 'Update the elective cycle for all institutions to the current year.'

    def handle(self, *args, **kwargs):
        # 1. Capture the current year from the system
        today = datetime.date.today()
        current_year = today.year
        
        # 2. Retrieve the cycle for the current year
        # Since your Repository doesn't have a 'get_by_year' method yet, 
        # we query the model directly using the 'year' field you defined.
        current_cycle = ElectiveCycle.objects.filter(
            year=current_year, 
            is_active=True
        ).first()
        
        if not current_cycle:
            self.stdout.write(
                self.style.ERROR(f'Update failed: No active elective cycle found for year {current_year}.')
            )
            return

        # 3. Fetch all institutions using YOUR Service
        institutions = InstitutionServices.get_all_institution()
        
        if not institutions:
            self.stdout.write(self.style.WARNING('No institutions found to update.'))
            return

        # 4. Process the massive update using YOUR Service method
        count = 0
        for inst in institutions:
            try:
                # Calling your specific method: update_elective_cycle_automatic(institution_id, elective_cycle_id)
                InstitutionServices.update_elective_cycle_automatic(
                    institution_id=inst.id,
                    elective_cycle_id=current_cycle.id
                )
                count += 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Could not update institution ID {inst.id}: {str(e)}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully synchronized {count} institutions to cycle {current_year}.')
        )