"""
Establishment Module API Views

This module provides the interface for managing all institutional entities, 
including physical addresses, administrative categories, core institution 
profiles, and historical records. It orchestrates the flow between HTTP 
requests, Service-layer business logic, and Serializer data representation.

Endpoints:
- Address: Full CRUD for physical locations.
- Categories: Management of institutional classifications.
- Institution: Core operations for educational entities.
- History: Archival and foundational record management.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from establishment.services.address import AddressServices
from establishment.services.institution_category import InstitutionCategoryServices
from establishment.services.institution import InstitutionServices
from establishment.services.history_institution import HistoryInstitutionServices

from establishment.serializers import (
    ListAddressSerializer,
    ListInstitutionCategorySerializer,
    ListInstitutionSerializer,
    ListHistoryInsitutionSerializer
)


# Views Address
class ListAddressView(APIView):
    # permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get(self, request):
        # Retrieves the complete directory of physical addresses.
        address = AddressServices.get_all_address()
        
        if not address:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListAddressSerializer(address, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class AddressByIdView(APIView):
    # permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Fetches a specific address record via its primary identifier.
        address_id = int(kwargs.get('id'))
        
        if not address_id:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = AddressServices.get_address_by_id(address_id)
        
        serializer = ListAddressSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class AddressByStreetView(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        # Queries addresses based on the street name attribute.
        address_street = str(kwargs.get('street'))
        
        if not address_street:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = AddressServices.get_address_by_street(address_street)
        
        serializer = ListAddressSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class AddressByCityView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Retrieves all addresses located within a specific administrative city.
        address_city = int(kwargs.get('id'))
        
        if not address_city:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = AddressServices.get_address_by_city(address_city)
        
        serializer = ListAddressSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class CreateAddressView(APIView):
    # permission_classes = [IsAdminUser]
    
    def post(self, request):
        # Orchestrates the creation of a new physical location.
        data = request.data

        try:
            # Validates that critical location data and city link are present.
            if not data or 'city_id' not in data:
                return Response({"Error": "Sensitive data is missing or the city ID is missing"}, status=status.HTTP_404_NOT_FOUND)
            
            response = AddressServices.create_address(
                data,
                data['city_id']
            )
            
            serializer = ListAddressSerializer(response)
            return Response({
                'Message': 'The address has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UpdateAddressView(APIView):
    # permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        # Coordinates the update of existing geographical address records.
        address_id = int(kwargs.get('id'))
        data = request.data
        
        try:
            if not data or 'city_id' not in data or not address_id:
                return Response({"Error": "Data is missing: city ID or address ID required"}, status=status.HTTP_404_NOT_FOUND)
             
            response = AddressServices.update_address(
                data,
                address_id,
                data['city_id']
            )
            
            serializer = ListAddressSerializer(response)
            return Response({
                'Message': 'The address has been successfully updated',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Views Institution Category

class ListInstitutionCategoryView(APIView):
    # permission_classes = [IsAdminUser]
    
    def get(self, request):
        # Lists all administrative classifications for educational entities.
        category = InstitutionCategoryServices.get_all_category()
    
        if not category:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListInstitutionCategorySerializer(category, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class InstitutionCategoryByIdView(APIView):
    # permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Finds a specific category by its unique primary key.
        category_id = int(kwargs.get('id'))
        
        if not category_id:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = InstitutionCategoryServices.get_category_by_id(category_id)
        
        serializer = ListInstitutionCategorySerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class InstitutionCategoryByNameView(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        # Filters categories using a descriptive name search.
        category_name = str(kwargs.get('name'))
        
        if not category_name:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = InstitutionCategoryServices.get_category_by_name(category_name)
        
        serializer = ListInstitutionCategorySerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


# Views Institution

class ListInstitutionView(APIView):
    def get(self, request):
        # Returns a complete list of all registered institutions and their status.
        institution = InstitutionServices.get_all_institution()
        
        if not institution:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListInstitutionSerializer(institution, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class InstitutionByIdView(APIView):
    # permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Retrieves the core profile of a single institution by ID.
        institution_id = int(kwargs.get('id'))
        
        if not institution_id:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        response = InstitutionServices.get_institution_by_id(institution_id)
        
        serializer = ListInstitutionSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class InstitutionByNameView(APIView):
    def get(self, request, *args, **kwargs):
        # Searches for institutions using a case-insensitive name filter.
        institution_name = str(kwargs.get('name'))
        
        if not institution_name:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = InstitutionServices.get_institution_by_name(institution_name)
        
        serializer = ListInstitutionSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class InstitutionByCityView(APIView):
    def get(self, request, *args, **kwargs):
        # Lists all institutions mapped to a specific administrative city.
        city_name = str(kwargs.get('name'))
        
        if not city_name:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = InstitutionServices.get_institution_by_city(city_name)
        
        serializer = ListInstitutionSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class InstitutionByCategoryView(APIView):
    def get(self, request, *args, **kwargs):
        
        category_name = str(kwargs.get('name'))
        
        if not category_name:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = InstitutionServices.get_institution_by_category(category_name)
        
        serializer = ListInstitutionSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

        
class CreateInstitutionView(APIView):
    # permission_classes = [IsAdminUser]
    
    def post(self, request):
        # Handles the registration of new educational entities.
        data = request.data
        
        try:
            # Validates cross-domain links: Category, Address, and Cycle.
            if not data or 'category_id' not in data or 'address_id' not in data or 'elective_cycle_id' not in data:
                return Response({"Error": "Missing link IDs: Category, Address, or Cycle"}, status=status.HTTP_404_NOT_FOUND)
            
            response = InstitutionServices.create_institution(
                data,
                data['category_id'],
                data['address_id'],
                data['elective_cycle_id']
            )
            
            serializer = ListInstitutionSerializer(response)
            return Response({
                'Message': 'The institution has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UpdateInstitutionView(APIView):
    # permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        # Manages modifications to institutional profiles and associations.
        data = request.data
        institution_id = int(kwargs.get('id'))
        
        try:
            if not data or not institution_id or 'category_id' not in data or 'address_id' not in data:
                return Response({"Error": "Critical update data is missing"}, status=status.HTTP_404_NOT_FOUND)

            response = InstitutionServices.update_institution(
                data,
                institution_id,
                data['category_id'],
                data['address_id'],
                data['elective_cycle_id']
            )
            
            serializer = ListInstitutionSerializer(response)
            return Response({
                'Message': 'The institution has been successfully updated',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Views History Institution

class ListHistoryInstitutionView(APIView):    
    def get(self, request):
        # Retrieves all biographical and foundational archives.
        history_institution = HistoryInstitutionServices.get_all_history()
        
        if not history_institution:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListHistoryInsitutionSerializer(history_institution, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class HistoryInstitutionByIdView(APIView):
    # permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Fetches a specific historical entry by unique ID.
        history_institution_id = int(kwargs.get('id'))
        
        if not history_institution_id:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = HistoryInstitutionServices.get_history_institutional_by_id(history_institution_id)
        
        serializer = ListHistoryInsitutionSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class HistoryInstitutionByInstitutionView(APIView):
    def get(self, request, *args, **kwargs):
        # Retrieves the legacy records belonging to a specific institution.
        instituiton_id = int(kwargs.get('id'))
        
        if not instituiton_id:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = HistoryInstitutionServices.get_history_institutional_by_institutional(instituiton_id)
        
        serializer = ListHistoryInsitutionSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class CreateHistoryInstitutionView(APIView):
    # permission_classes = [IsAdminUser]
    
    def post(self, request):
        # Registers a new historical narrative for an institution.
        data = request.data
        
        try:
            if not data or 'institution_id' not in data:
                return Response({"Error": "Missing parent Institution ID"}, status=status.HTTP_404_NOT_FOUND)

            response = HistoryInstitutionServices.create_history_institution(
                data,
                data['institution_id']
            )
            
            serializer = ListHistoryInsitutionSerializer(response)
            return Response({
                'Message': 'The history institution has been successfully created',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateHistoryInstitutionView(APIView):
    # permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        # Modifies institutional biography or foundational data.
        data = request.data
        history_institution_id = int(kwargs.get('id'))
        
        try:
            if not data or 'institution_id' not in data or not history_institution_id:
                return Response({"Error": "Missing historical record or institution link ID"}, status=status.HTTP_404_NOT_FOUND)
            
            response = HistoryInstitutionServices.update_history_institution(
                data,
                history_institution_id,
                data['institution_id']
            )
            
            serializer = ListHistoryInsitutionSerializer(response)
            return Response({
                'Message': 'The history institution has been successfully updated',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)