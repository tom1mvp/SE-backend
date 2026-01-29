from rest_framework import serializers


from grades.models import AssessmentCategory, Grade


class ListAssessmentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentCategory
        fields = '__all__'
        
class ListGradeSerializer(serializers.ModelSerializer):
    subject_name = serializers.SerializerMethodField()
    student_first_name = serializers.SerializerMethodField()
    student_last_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Grade
        fields = [
			'id',
			'number',
			'date',
			'term',
			'subject_name',
			'student_first_name',
   			'student_last_name',
			'category_name',
		]
    
    def get_subject_name(self, obj):
        return obj.subject.name
    
    def get_student_first_name(self, obj):
        return obj.student.person.first_name
    
    def get_student_last_name(self, obj):
        return obj.student.person.last_name
    
    def get_category_name(self, obj):
        return obj.category.name if obj.category else None