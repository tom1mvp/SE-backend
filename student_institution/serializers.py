from rest_framework import serializers


from student_institution.models import AllergyKind, Student, StudentFile, SubjectEnrollment

class ListStudentSerializer(serializers.ModelSerializer):
    person_id = serializers.SerializerMethodField()
    student_first_name = serializers.SerializerMethodField()
    student_last_name = serializers.SerializerMethodField()
    student_mail = serializers.SerializerMethodField()
    student_file_number = serializers.SerializerMethodField()
    student_file_date_admission = serializers.SerializerMethodField()
    student_file_photo_url = serializers.SerializerMethodField()
    institution_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Student
        fields = [
            'id',
            'person_id',
            'student_first_name',
            'student_last_name',
            'student_mail',
            'student_file_number',
            'student_file_date_admission',
            'student_file_photo_url',
            'institution_name',
            'is_active'
        ]
    
    def get_person_id(self, obj):
        return obj.person.id
    
    def get_student_first_name(self, obj):
        return obj.person.first_name
    
    def get_student_last_name(self, obj):
        return obj.person.last_name
    
    def get_student_mail(self, obj):
        return obj.person.mail
    
    def get_student_file_number(self, obj):
        return obj.student_file.number
    
    def get_student_file_date_admission(self, obj):
        return obj.student_file.date_admission
    
    def get_student_file_photo_url(self, obj):
        return obj.student_file.photo_url if obj.student_file.photo_url else None
    
    def get_institution_name(self, obj):
        return obj.student_file.institution.name
    
class ListStudentFileSerializer(serializers.ModelSerializer):
    institution_name = serializers.SerializerMethodField()
    allergy_name = serializers.SerializerMethodField()
    
    class Meta:
        model = StudentFile
        fields = [
            'id',
            'number',
            'date_admission',
            'is_allergic',
            'photo_url',
            'social_work_name',
            'social_work_number',
            'emergency_contact_name',
            'emergency_contact_phone',
            'status',
            'institution_name',
            'allergy_name'
        ]
    
    def get_institution_name(self, obj):
        return obj.institution.name
    
    def get_allergy_name(self, obj):
        return obj.allergy.name
    
class ListSubjectEnrollmentSerializer(serializers.ModelSerializer):
    person_id = serializers.SerializerMethodField()
    student_first_name = serializers.SerializerMethodField()
    student_last_name = serializers.SerializerMethodField()
    subject_name = serializers.SerializerMethodField()
    elective_cycle_year = serializers.SerializerMethodField()
    
    class Meta:
        model = SubjectEnrollment
        fields = [
            'id',
            'person_id',
            'subject',
            'student',
            'student_first_name',
            'student_last_name',
            'subject_name',
            'elective_cycle_year'
        ]
        
    def get_elective_cycle_year(self, obj):
        return obj.elective_cycle.year
    
    def get_person_id(self, obj):
        return obj.student.person.id
    
    def get_student_first_name(self, obj):
        return obj.student.person.first_name
    
    def get_student_last_name(self, obj):
        return obj.student.person.last_name

    def get_subject_name(self, obj):
        return obj.subject.name
    
class ListAllergyKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllergyKind
        fields = '__all__'