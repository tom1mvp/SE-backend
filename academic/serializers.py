from rest_framework import serializers


from academic.models import ElectiveCycle, Subject


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