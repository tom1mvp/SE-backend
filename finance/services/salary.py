from rest_framework.validators import ValidationError
from finance.repositories.salary import TeacherSalaryRepository

"""
    Teacher Salary Service Layer
    
    This module acts as the intermediary between the API views and the Salary Repository.
    It implements business logic, data validation, and ensures that financial 
    records meet institutional requirements before being persisted.
"""

class TeacherSalaryServices:
    # Acts as a proxy to retrieve the complete collection of salary records.
    @staticmethod
    def get_all_salary():
        return TeacherSalaryRepository.get_all_salary()
    
    # Coordinates the retrieval of a specific compensation entry.
    @staticmethod
    def get_salary_by_id(salary_id):
        return TeacherSalaryRepository.get_salary_by_id(salary_id)
    
    # Business logic for filtering payroll history by specific dates.
    @staticmethod
    def get_salary_by_date(date):
        return TeacherSalaryRepository.get_salary_by_date(date)
    
    # Facilitates specialized lookups for salary history linked to a specific teacher.
    @staticmethod
    def get_salary_by_teacher(teacher_id):
        return TeacherSalaryRepository.get_salary_by_teacher(teacher_id)
    
    # Handles the complex creation process including payload validation.
    @staticmethod
    def create_salary(
      data,
      file_id  
    ):
        # Definition of essential attributes for a valid financial record.
        required_fields = [
            'payment_date',
            'status',
            'amount',
            'paymethod',
            'period'
        ]
        
        # Data Integrity Check: Enforcing mandatory fields before database insertion.
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValidationError({field: f'The field {field} is mandatory.'})
            
        # Delegates the record persistence to the repository layer.
        new_salary = TeacherSalaryRepository.create_salary(
            payment_date=data['payment_date'],
            status=data['status'],
            amount=data['amount'], # Added amount field to match your repository
            paymethod=data['paymethod'], # Corrected key from 'paymenthod'
            period=data['period'],
            file_id=file_id
        )
        
        return new_salary
    
    # Manages the update workflow for existing salary records.
    @staticmethod
    def update_salary(
        data,
        salary_id,
    ):
        # Triggers the repository update logic with validated data.
        salary = TeacherSalaryRepository.update_salary(
            salary_id=salary_id,
            payment_date=data['payment_date'],
            status=data['status'],
            amount=data['amount'], # Added amount for consistency
            paymethod=data['paymethod'], # Corrected key from 'paymenthod'
            period=data['period']
        )
        
        return salary