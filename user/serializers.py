from django.contrib.auth.hashers import make_password


from rest_framework import serializers


from .models import User



class UserSerializer(serializers.ModelSerializer):
    
    # Hash for password
    class Meta:
        model=User
        fields='__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
            
        return super().create(validated_data)
        
class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id', 'username', 'image', 'role', 'is_active']