import datetime


from django.core.management.base import BaseCommand


from academic.services.elective_cycle import ElectiveCycleServices

class Command(BaseCommand):
    """
    Academic Year Automation Command
    
    This command serves as the automated entry point for managing the school's 
    chronological lifecycle. It is designed to be executed daily via Cron Job, 
    but only triggers database changes on specific institutional dates.
    
    Scheduled Events:
    - February 26th: Opening of the new academic cycle.
    - December 15th: Official closing and deactivation of the current cycle.
    """
    
    help = 'Review and execute the opening or closing of the academic year.'

    def handle(self, *args, **kwargs):
        # Capture the current date for validation
        today = datetime.date.today()
        current_year = today.year
    
        # Define the exact dates for institutional transitions
        open_date = datetime.date(current_year, 2, 26)
        close_date = datetime.date(current_year, 12, 15)
    
        # Logic to determine if a state change is required today
        if today == open_date:
            # Trigger the creation process for the current year
            result = ElectiveCycleServices.create_elective_cycle()
            self.stdout.write(self.style.SUCCESS(f'Successfully opened elective cycle: {result}'))
            
        elif today == close_date:
            # Trigger the deactivation of all cycles reaching their end date
            result = ElectiveCycleServices.disable_elective_cycle()
            self.stdout.write(self.style.SUCCESS(f'Successfully closed elective cycle: {result}'))
            
        else:
            # Informative message when no action is needed
            self.stdout.write(self.style.WARNING(f'Today ({today}) is not a scheduled date for cycle changes.'))