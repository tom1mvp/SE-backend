from academic.models import ModalityAssistance


class ModalityAssistanceRepository:
    @staticmethod
    def create_modality_assistance(
        name
    ):
        new_modality_assistance = ModalityAssistance.objects.create(
            name=name
        )
        
        return new_modality_assistance
    
    