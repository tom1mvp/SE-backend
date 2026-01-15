from rest_framework import serializers


from finance.models import TeacherSalary


class ListTeacherSalarySerializer(serializers.ModelSerializer):
    file_id = serializers.SerializerMethodField()
    file_number = serializers.SerializerMethodField()
    class Meta:
        model = TeacherSalary
        fields = [
            'id',
            'payment_date',
            'status',
            'amount',
            'paymethod',
            'period',
            'file_id',
            'file_number'
        ]
        
    def get_file_id(self, obj):
        return obj.file.id
    
    def get_file_number(self, obj):
        return obj.file.number
    
    