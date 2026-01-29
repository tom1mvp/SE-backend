from rest_framework import serializers


from relationship.models import Relationship


class ListRelationshipSerializer(serializers.ModelSerializer):
    tutor_id = serializers.SerializerMethodField()
    tutor_first_name = serializers.SerializerMethodField()
    tutor_last_name = serializers.SerializerMethodField()
    
    student_id = serializers.SerializerMethodField()
    student_first_name = serializers.SerializerMethodField()
    student_last_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Relationship
        fields = [
			'id',
			'kinship',
			'description',
			'tutor_id',
			'tutor_first_name',
			'tutor_last_name',
			'student_id',
			'student_first_name',
			'student_last_name',
			'is_active'
		]
    
    def get_tutor_id(self, obj):
        return obj.tutor.id
    
    def get_tutor_first_name(self, obj):
        return obj.tutor.person.first_name
    
    def get_tutor_last_name(self, obj):
        return obj.tutor.person.last_name
    
    def get_student_id(self, obj):
        return obj.student.id
    
    def get_student_first_name(self, obj):
        return obj.student.person.first_name
    
    def get_student_last_name(self, obj):
        return obj.student.person.last_name