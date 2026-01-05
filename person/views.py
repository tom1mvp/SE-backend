"""
Person Management Views

This module centralizes the administrative logic for all person-related entities
within the school system (Genre, Identity Documents, and Marital Status).
It serves as the entry point for managing the personal data lifecycle of
students, staff, and guardians—from their initial registration and
identification to their eventual recovery or deactivation.

Current Functionalities (GET):
- List all available classifications (Genres, Document Types, Marital Status).
- Retrieve specific records by unique ID for precise data binding.
- Search classifications by name/description for dynamic UI filtering.

Upcoming Functionalities (CRUD Operations):
- POST: Register new identity classifications and personal data records.
- PUT: Full updates for modifying legal or demographic information.
- PATCH:
    * Soft delete (Deactivation) for archiving personal records while preserving history.
    * Recovery (Reactivation) to restore previously deactivated accounts or profiles.
"""


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from person.services.genre import GenreServices
from person.services.identity_document import IdentityDocumentServices
from person.services.marital_status import MaritalStatusServices
from person.services.person import PersonServices


from person.serializers import (
        GenreListSerializer,
        IdentityDocumentListSerializer,
        MaritalStatusListSerializer,
        PersonListSerializer
    )

# Views Genre
class ListGenreView(APIView):
    
    permission_classes = [IsAdminUser]
    def get(self, request):
        genre = GenreServices.get_all_genre()
        
        if not genre:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = GenreListSerializer(genre, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class GenreByIdView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, *args, **kwargs):
        genre_id = int(kwargs.get('id'))
        
        if not genre_id:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = GenreServices.get_genre_by_id(genre_id)
        
        serializer = GenreListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class GenreByNameView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, *args, **kwargs):
        genre_name = str(kwargs.get('name'))
        
        if not genre_name:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = GenreServices.get_genre_by_name(genre_name)
        
        serializer = GenreListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
# Views indetity document
class ListIdentityDocumentView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        indetity_document = IdentityDocumentServices.get_all_identity_document()
        
        if not indetity_document:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = IdentityDocumentListSerializer(indetity_document, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class IdentityDocumentByIdView(APIView):
        permission_classes = [IsAdminUser]
        
        def get(self, request, *args, **kwargs):
            identity_document_id = int(kwargs.get('id'))
            
            if not identity_document_id:
                return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
            
            response = IdentityDocumentServices.get_identity_document_by_id(identity_document_id)
            
            serializer = IdentityDocumentListSerializer(response)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class IdetityDocumentByNameView(APIView):
    permission_classes = [IsAdminUser]
        
    def get(self, request, *args, **kwargs):
        identity_document_name = str(kwargs.get('name'))
        
        if not identity_document_name:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = IdentityDocumentServices.get_identity_document_by_name(identity_document_name)
        
        serializer = IdentityDocumentListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
# Views Marital status
class ListMaritalStatusView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        marital_status = MaritalStatusServices.get_all_marital_status()
        
        if not marital_status:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MaritalStatusListSerializer(marital_status, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class MaritalStatusByIdView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        marital_status_id = int(kwargs.get('id'))
        
        if not marital_status_id:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        response = MaritalStatusServices.get_marital_status_by_id(marital_status_id)
        
        serializer = IdentityDocumentListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class MaritalStatusByNameView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        marital_status_name = str(kwargs.get('name'))
        
        if not marital_status_name:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = MaritalStatusServices.get_marital_status_by_name(marital_status_name)
        
        serializer = IdentityDocumentListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
# Views person
class ListPersonView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        # Retrieve the complete list of person profiles.
        person = PersonServices.get_all_person()
        
        if not person:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonListSerializer(person, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class PersonByIdView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Fetch a specific person profile using its primary key.
        person_id = int(kwargs.get('id'))
        
        if not person_id:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = PersonServices.get_person_by_id(person_id)
        
        serializer = PersonListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class PersonByNameView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Filter person profiles by a partial match of their first name.
        person_name = str(kwargs.get('name'))
        
        if not person_name:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = PersonServices.get_person_by_name(person_name)
        
        serializer = PersonListSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class PersonByUserView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Retrieve the person profile linked to a specific User account ID.
        user_id = int(kwargs.get('id'))
        
        if not user_id:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response = PersonServices.get_person_by_user(user_id)
        
        serializer = PersonListSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class CreatePersonView(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        # Handle the creation of a new person record with validated relations.
        data = request.data
        
        try:
            if not data or 'city_id' not in data:
                return Response({"Error": "Sensitive data is missing or the city ID is missing"}, status=status.HTTP_404_NOT_FOUND)
            
            response = PersonServices.create_person(
                data,
                data['user_id'],
                data['genre_id'],
                data['marital_status_id'],
                data['identity_document_id'],
                data['city_id']
            )
            serializer = PersonListSerializer(response)
            
            return Response({
                'Message': 'The person has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdatePersonView(APIView):
    permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        # Execute a full update of an existing person's information.
        person_id = int(kwargs.get('id'))
        data = request.data
        
        try:
            if not data or not person_id or 'city_id' not in data:
                return Response({"Error": "Sensitive data is missing or the city ID is missing or the person ID is missing"}, status=status.HTTP_404_NOT_FOUND)
            
            response = PersonServices.update_person(
                data,
                person_id,
                data['user_id'],
                data['genre_id'],
                data['marital_status_id'],
                data['identity_document_id'],
                data['city_id']
            )
            
            serializer = PersonListSerializer(response)
            
            return Response({
                'Message': 'The person has been successfully updated',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DeletePersonView(APIView):
    permission_classes = [IsAdminUser]
    
    def patch(self, request, *args, **kwargs):
        # Deactivate a person record (logical delete) to preserve institutional history.
        person_id = int(kwargs.get('id'))
        
        try:
            PersonServices.delete_person(person_id)
            return Response({'message': 'The person was successfully deactivated.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class RecoverPersonView(APIView):
    permission_classes = [IsAdminUser]
    
    def patch(self, request, *args, **kwargs):
        # Restore an inactive person profile to active status in the system.
        person_id = int(kwargs.get('id'))
        
        try:
            PersonServices.recover_person(person_id)
            return Response({'message': 'The person was successfully recovered.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)