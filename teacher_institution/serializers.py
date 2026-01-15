from rest_framework import serializers
from teacher_institution.models import (
    Teacher,
    TeachingAssistance,
    TeachingFile
)

class ListTeachingFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingFile
        fields = '__all__'
        

class ListTeachingAssistanceSerializer(serializers.ModelSerializer):
    teacher_id = serializers.SerializerMethodField()
    teacher_name = serializers.SerializerMethodField()
    teacher_last_name = serializers.SerializerMethodField()
    
    class Meta:
        model = TeachingAssistance
        fields = [
            'id',
            'date',
            'reason',
            'observation',
            'teacher_id',
            'teacher_name',
            'teacher_last_name',
        ]
    
    def get_teacher_id(self, obj):
        return obj.teacher.id
    
    def get_teacher_name(self, obj):
        return obj.teacher.person.first_name
    
    def get_teacher_last_name(self, obj):
        return obj.teacher.person.last_name

class ListTeacherSerializer(serializers.ModelSerializer):
    teacher_name = serializers.SerializerMethodField()
    teacher_last_name = serializers.SerializerMethodField()
    teacher_number_document = serializers.SerializerMethodField()
    teacher_mail = serializers.SerializerMethodField()
    file_number = serializers.SerializerMethodField()
    file_license_number = serializers.SerializerMethodField()
    
    class Meta:
        model = Teacher
        fields = [
            'id',
            'teacher_name',
            'teacher_last_name',
            'teacher_number_document',
            'teacher_mail',
            'file_number',
            'file_license_number'
        ]
    
    def get_teacher_name(self, obj):
        return obj.person.first_name
    
    def get_teacher_last_name(self, obj):
        return obj.person.last_name
    
    def get_teacher_number_document(self, obj):
        return obj.person.number_document
    
    def get_teacher_mail(self, obj):
        return obj.person.mail
    
    def get_file_number(self, obj):
        return obj.file.number
    
    def get_file_license_number(self, obj):
        return obj.file.license_number