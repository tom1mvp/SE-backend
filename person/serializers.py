from rest_framework import serializers


from person.models import Genre, IdentityDocument, MaritalStatus


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