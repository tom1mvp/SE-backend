from rest_framework import serializers


from academic.models import ElectiveCycle


class ListElectiveCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model=ElectiveCycle
        fields = '__all__'