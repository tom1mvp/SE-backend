from finance.models import TeacherSalary
from teacher_institution.models import TeachingFile


"""
    Teacher Salary Repository
    
    This module handles direct database interactions for teacher compensation records.
    It encapsulates the logic for retrieving, creating, and updating salary data,
    acting as a clean abstraction layer between the database and the service layer.
"""


class TeacherSalaryRepository:
    # Fetches all payroll records registered in the financial system.
    @staticmethod
    def get_all_salary():
        return TeacherSalary.objects.all()
    
    # Locates a specific salary entry by its primary key.
    @staticmethod
    def get_salary_by_id(salary_id):
        return TeacherSalary.objects.filter(id=salary_id).first()
    
    # Retrieves all compensation records issued on a specific calendar date.
    @staticmethod
    def get_salary_by_date(date):
        return TeacherSalary.objects.filter(payment_date=date)
    
    # Returns the salary record for a teacher by traversing the File-Teacher relationship.
    @staticmethod
    def get_salary_by_teacher(teacher_id):
        return TeacherSalary.objects.filter(file__teacher__id=teacher_id).first()
    
    # Orchestrates the creation of a new payroll entry linked to a Teaching File.
    @staticmethod
    def create_salary(
        payment_date,
        status,
        amount,
        paymethod,
        period,
        file_id
    ):
        # Verification of the institutional professional record before issuance.
        file = TeachingFile.objects.filter(id=file_id).first()
        
        if not file:
            raise ValueError('Error', 'File not found')
        
        # Persists the financial record into the database.
        new_salary = TeacherSalary.objects.create(
            payment_date=payment_date,
            status=status,
            amount=amount,
            paymethod=paymethod,
            period=period,
            file=file
        )
        
        return new_salary
    
    # Modifies an existing compensation record ensuring the integrity of the transaction.
    @staticmethod
    def update_salary(
        salary_id,
        payment_date,
        status,
        amount,
        paymethod,
        period
    ):
        # Locates the record for modification.
        salary = TeacherSalary.objects.filter(id=salary_id).first()
        
        if not salary:
            raise ValueError('error', 'Salary not found')

        # Atomic updates of financial attributes.
        salary.payment_date=payment_date
        salary.status=status
        salary.amount=amount
        salary.paymethod=paymethod
        salary.period=period
        
        salary.save()
        
        return salary