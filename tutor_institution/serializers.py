from rest_framework import serializers


from tutor_institution.models import Tutor


class ListTutorSerializer(serializers.ModelSerializer):
    
    person_id = serializers.SerializerMethodField()
    person_first_name = serializers.SerializerMethodField()
    person_last_name = serializers.SerializerMethodField()
    person_mail = serializers.SerializerMethodField()
    person_dni = serializers.SerializerMethodField()
    
    class Meta:
        model = Tutor
        fields = [
            'id',
            'person_id',
            'person_first_name',
            'person_last_name',
            'person_mail',
            'person_dni'
        ]
    
    def get_person_id(self, obj):
        return obj.person.id
    
    def get_person_first_name(self, obj):
        return obj.person.first_name
    
    def get_person_last_name(self, obj):
        return obj.person.last_name
    
    def get_person_mail(self, obj):
        return obj.person.mail
    
    def get_person_dni(self, obj):
        return obj.person.number_document