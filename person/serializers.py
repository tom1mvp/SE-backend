from rest_framework import serializers


from person.models import (
        Genre,
        IdentityDocument,
        MaritalStatus,
        Person
    )


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields='__all__'
        
class IdentityDocumentListSerializer(serializers.ModelSerializer):
    class Meta:
        model=IdentityDocument
        fields='__all__'

class MaritalStatusListSerializer(serializers.ModelSerializer):
     class Meta:
        model=MaritalStatus
        fields='__all__'
        

class PersonListSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    genre = serializers.SerializerMethodField()
    marital_status = serializers.SerializerMethodField()
    identity_document = serializers.SerializerMethodField()
    city_id = serializers.SerializerMethodField()
    city_name = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = [
            'id',
            'first_name',
            'last_name',
            'mail',
            'number_document',
            'date_of_birth',
            'phone',
            'genre',
            'marital_status',
            'identity_document',
            'city_id',
            'city_name',
            'user_id',
            'username',
            'is_active'
        ]
    
    def get_user_id(self, obj):
        return obj.user.id
    
    def get_username(self, obj):
        return obj.user.username
    
    def get_genre(self, obj):
        return obj.genre.name
    
    def get_marital_status(self, obj):
        return obj.marital_status.name
    
    def get_identity_document(self, obj):
        return obj.identity_document.name
    
    def get_city_id(self, obj):
        return obj.city.id
    
    def get_city_name(self, obj):
        return obj.city.name