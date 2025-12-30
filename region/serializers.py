from rest_framework import serializers


from .models import Country, Province, City


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields='__all__'
        
class ProvinceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields='__all__'
        
class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields='__all__'