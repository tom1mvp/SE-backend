from rest_framework import serializers


from academic.models import (
    ElectiveCycle, Subject,
    ModalityAssistance,
    Assistance,
    DisciplinaryAction,
    Course
)


class ListElectiveCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model=ElectiveCycle
        fields = '__all__'
    
class ListSubjectSerializer(serializers.ModelSerializer):
    course_id = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()
    
    teacher_id = serializers.SerializerMethodField()
    teacher_first_name = serializers.SerializerMethodField()
    teacher_last_name = serializers.SerializerMethodField()
    class Meta:
        model = Subject
        fields = [
            'id',
            'course_id',
            'name',
            'course_name',
            'start_time',
            'end_time',
            'is_active',
            'teacher_id',
            'teacher_first_name',
            'teacher_last_name'
        ]
    
    def get_course_id(self, obj):
        return obj.course.id
    
    def get_course_name(self, obj):
        return obj.course.name
    
    def get_teacher_id(self, obj):
        return obj.teacher.id
    
    def get_teacher_first_name(self, obj):
        return obj.teacher.person.first_name
    
    def get_teacher_last_name(self, obj):
        return obj.teacher.person.last_name
    
    
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
    
    
class ListCourseSerializer(serializers.ModelSerializer):
    institution_id = serializers.SerializerMethodField()
    institution_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
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