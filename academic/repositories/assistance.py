from academic.models import Assistance, ModalityAssistance
from student_institution.models import Student


class AssistanceRepository:
    @staticmethod
    def get_all_assistance():
        return Assistance.objects.all()
    
    @staticmethod
    def get_assistance_by_student(student_id):
        return Assistance.objects.filter(student__id=student_id).first()
    
    @staticmethod
    def get_assistance_by_date(date):
        return Assistance.objects.filter(date=date)
    
    @staticmethod
    def create_assistance(
      date,
      observation,
      modality_id,
      student_id,
      is_absence
    ):
        
        modality = ModalityAssistance.objects.filter(id=modality_id).first()
        
        if not modality:
            raise ValueError('error', 'Modality not found')
        
        student = Student.objects.filter(id=student_id).first()
        
        if not student:
            raise ValueError('error', 'Student not found')
        
        new_assistance = Assistance.objects.create(
            date=date,
            observation=observation,
            modality=modality,
            student=student,
            is_absence=is_absence
        )
        
        return new_assistance
    
    
    @staticmethod
    def update_assistance(
        assistance_id,
        date,
        observation,
        modality_id,
        student_id,
        is_absence
    ):
        assistance = Assistance.objects.filter(id=assistance_id).first()
        
        if not assistance:
            raise ValueError('error', 'Assistance not found')
        
        modality = ModalityAssistance.objects.filter(id=modality_id).first()
        
        if not modality:
            raise ValueError('error', 'Modality not found')
        
        student = Student.objects.filter(id=student_id).first()
        
        if not student:
            raise ValueError('error', 'Student not found')
        
        assistance.date=date
        assistance.observation=observation
        assistance.modality=modality
        assistance.student=student
        assistance.is_absence=is_absence
        
        assistance.save()
        
        return assistance
    
    