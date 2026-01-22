from academic.models import DisciplinaryAction
from student_institution.models import Student


class DisciplinaryActionRepository:
    @staticmethod
    def get_all_disciplinary_action():
        return DisciplinaryAction.objects.all()
    
    @staticmethod
    def get_disciplinary_action_by_date(date):
        return DisciplinaryAction.objects.filter(date=date)
    
    @staticmethod
    def get_disciplinary_action_by_student(name):
        return DisciplinaryAction.objects.filter(student__person__first_name__icontains=name).first()
    
    
    @staticmethod
    def create_disciplinary_action(
        date,
        reason,
        quantity,
        observation,
        student_id
    ):
        
        student = Student.objects.filter(id=student_id).first()
        
        if not student:
            raise ValueError('error', 'Student not found')
        
        new_disciplinary_action = DisciplinaryAction.objects.create(
            date=date,
            reason=reason,
            quantity=quantity,
            observation=observation,
            student=student
        )
        
        return new_disciplinary_action
    
    @staticmethod
    def update_disciplinary_action(
        disciplinary_action_id,
        date,
        reason,
        quantity,
        observation,
        student_id
    ):
        disciplinary_action = DisciplinaryAction.objects.filter(id=disciplinary_action_id).first()
        
        if not disciplinary_action:
            raise ValueError('Disciplinary action not found')
        
        student = Student.objects.filter(id=student_id).first()
        
        if not student:
            raise ValueError('Student not found')
        
        disciplinary_action.date = date
        disciplinary_action.reason = reason
        disciplinary_action.quantity = quantity
        disciplinary_action.observation = observation
        disciplinary_action.student = student
        
        disciplinary_action.save()
        
        return disciplinary_action