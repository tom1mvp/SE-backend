from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser

from region.services.country import CountryServices
from region.services.province import ProvinceServices
from region.services.city import CityServices


from region.serializers import (
    CountryListSerializer,
    ProvinceListSerializer,
    CityListSerializer
    )

# View's country
class ListCountryView(APIView):
    """
    Provides a list of all registered countries.
    Access restricted to administrators.
    """
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        # Fetch all countries from the service layer
        country = CountryServices.get_all_country()
        
        if not country:
            # Return error if no data is found
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize and return the country collection
        serializer = CountryListSerializer(country, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class CountryByIdView(APIView):
    """
    Retrieves a single country instance based on its ID.
    """
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Extract and validate the ID from URL parameters
        country_id = int(kwargs.get('id'))
        
        if not country_id:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Get specific country and serialize result
        response = CountryServices.get_country_by_id(country_id)
        serializer = CountryListSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class CountryByNameView(APIView):
    """
    Filters countries by name for search or autocomplete functionality.
    """
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Extract country name from path
        country_name = str(kwargs.get('name'))
        
        if not country_name:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Perform search and serialize matching results
        response = CountryServices.get_country_by_name(country_name)
        serializer = CountryListSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

# View's provice
class ListProvinceView(APIView):
    """
    Provides a list of all administrative provinces.
    """
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        # Retrieve complete list of provinces
        province = ProvinceServices.get_all_provinces()
        
        if not province:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the province queryset
        serializer = ProvinceListSerializer(province, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class ProvinceByIdView(APIView):
    """
    Retrieves a specific province by its primary key.
    """
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Obtain ID from request parameters
        province_id = int(kwargs.get('id'))
        
        if not province_id:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Fetch data from service and serialize
        response = ProvinceServices.get_province_by_id(province_id)
        serializer = ProvinceListSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class ProvinceByNameView(APIView):
    """
    Searches for provinces based on a string match.
    """
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Extract search term
        province_name = str(kwargs.get('name'))
        
        if not province_name:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Execute search and serialize results
        response = ProvinceServices.get_province_by_name(province_name)
        serializer = ProvinceListSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class ProvinceByCountryView(APIView):
    """
    Lists all provinces that belong to a specific country.
    """
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Extract parent country identifier
        country_id = int(kwargs.get('id'))
        
        if not country_id:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Filter provinces by parent country ID
        response = ProvinceServices.get_province_by_country(country_id)
        serializer = ProvinceListSerializer(response, many=True)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


# View's city
class ListCityView(APIView):
    """
    Provides a global list of all cities/localities.
    """
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        # Call service to get all cities
        city = CityServices.get_all_city()
        
        if not city:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Return serialized city data
        serializer = CityListSerializer(city, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class CityByIdView(APIView):
    """
    Retrieves city details based on its ID.
    """
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Get city ID from parameters
        city_id = int(kwargs.get('id'))
        
        if not city_id:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Retrieve locality and serialize
        response = CityServices.get_city_by_id(city_id)
        serializer = CityListSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class CityByNameView(APIView):
    """
    Filters cities using a name search string.
    """
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Extract locality name
        city_name = str(kwargs.get('name'))
        
        if not city_name:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Fetch matching cities from service
        response = CityServices.get_city_by_name(city_name)
        serializer = CityListSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class CityByProvinceView(APIView):
    """
    Lists all cities that belong to a specific province.
    """
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Extract parent province identifier
        province_id = int(kwargs.get('id'))
        
        if not province_id:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Filter localities by parent province ID
        response = CityServices.get_city_by_province(province_id)
        serializer = CityListSerializer(response, many=True)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)