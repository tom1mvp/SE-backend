from rest_framework import serializers


from academic.models import ElectiveCycle, Subject, ModalityAssistance, Assistance, DisciplinaryAction


class ListElectiveCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model=ElectiveCycle
        fields = '__all__'
    
class ListSubjectSerializer(serializers.ModelSerializer):
    institution_id = serializers.SerializerMethodField()
    institution_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Subject
        fields = [
            'id',
            'name',
            'section',
            'time_slot',
            'institution_id',
            'institution_name'
        ]
    
    def get_institution_id(self, obj):
        return obj.institution.id
    
    def get_institution_name(self, obj):
        return obj.institution.name
    
    
class ListModalityAssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModalityAssistance
        fields = '__all__'
    
class ListAssistanceSerializer(serializers.ModelSerializer):
    student_id = serializers.SerializerMethodField()
    student_first_name = serializers.SerializerMethodField()
    student_last_name = serializers.SerializerMethodField()
    modality_name = serializers.SerializerMethodField()
    class Meta:
        model = Assistance
        fields = [
            'id',
            'date',
            'observation',
            'modality_name',
            'student_id',
            'student_first_name',
            'student_last_name',
            'is_absence'
        ]
        
    def get_student_id(self, obj):
        return obj.student.id
    
    def get_student_first_name(self, obj):
        return obj.student.person.first_name
    
    def get_student_last_name(self, obj):
        return obj.student.person.last_name
    
    def get_modality_name(self, obj):
        return obj.modality.name
    
class ListDisciplinaryActionSerializer(serializers.ModelSerializer):
    student_id = serializers.SerializerMethodField()
    student_first_name = serializers.SerializerMethodField()
    student_last_name = serializers.SerializerMethodField()
    
    class Meta:
        model = DisciplinaryAction
        fields = [
            'id',
            'date',
            'reason',
            'quantity',
            'observation',
            'student_id',
            'student_first_name',
            'student_last_name',
        ]
        
    def get_student_id(self, obj):
        return obj.student.id
    
    def get_student_first_name(self, obj):
        return obj.student.person.first_name
    
    def get_student_last_name(self, obj):
        return obj.student.person.last_name