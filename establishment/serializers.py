from rest_framework import serializers


from establishment.models import Address, InstitutionCategory, Institution, HistoryInstitution


class ListAddressSerializer(serializers.ModelSerializer):
    city_id = serializers.SerializerMethodField()
    city_name = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Address
        fields = [
            'id',
            'street',
            'number',
            'comment',
            'city_id',
            'city_name'
        ]
    
    def get_city_id(self, obj):
        return obj.city.id
    
    def get_city_name(self, obj):
        return obj.city.name

class ListInstitutionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionCategory
        fields = '__all__'

class ListInstitutionSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    address_street = serializers.SerializerMethodField()
    address_number = serializers.SerializerMethodField()
    address_city = serializers.SerializerMethodField()
    elective_cycle_year = serializers.SerializerMethodField()
    
    class Meta:
        model = Institution
        fields = [
            'id',
            'category_name',
            'name',
            'address_city',
            'address_street',
            'address_number',
            'opening_hour',
            'closing_hour',
            'elective_cycle_year',
            'logo_url',
            'is_active'
        ]
    
    def get_category_name(self, obj):
        return obj.category.name
    
    def get_address_street(self, obj):
        return obj.address.street
    
    def get_address_number(self, obj):
        return obj.address.number
    
    def get_address_city(self, obj):
        return obj.address.city.name
    
    def get_elective_cycle_year(self, obj):
        return obj.elective_cycle.year
    
class ListHistoryInsitutionSerializer(serializers.ModelSerializer):
    institution_id = serializers.SerializerMethodField()
    institution_name = serializers.SerializerMethodField()
    
    
    class Meta:
        model = HistoryInstitution
        fields = [
            'id',
            'institution_id',
            'institution_name',
            'biography',
            'foundation_date',
            'founder',
            'multimedia_url'
        ]
    
    def get_institution_id(self, obj):
        return obj.institution.id,
    
    def get_institution_name(self, obj):
        return obj.institution.name
    
    