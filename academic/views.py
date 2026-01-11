"""
This module implements the API endpoints for the Subject entity using Django Rest Framework's APIView.
The architecture follows a strict Separation of Concerns (SoC) principle where:
1. The View Layer: Intercepts HTTP requests (GET, POST, PUT), extracts parameters from the URL or body, 
   and delegates all business logic to the Service Layer.
2. The Service Layer (SubjectServices): Orchestrates data validation and coordinates with the 
   Repository for database persistence.
3. The Serialization Layer (ListSubjectSerializer): Transforms complex Django model instances 
   into native Python data types that can be easily rendered into JSON for the client.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from academic.services.subject import SubjectServices
from academic.serializers import ListSubjectSerializer

class ListSubjectView(APIView):
    permission_classes = [IsAuthenticated]
   
    def get(self, request):
        """Retrieves all subjects and returns a list of serialized data."""
        subject = SubjectServices.get_all_subject()
       
        if not subject:
            return Response(
                {
                    'error': 'List subject not found'
                }, status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ListSubjectSerializer(subject, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
class SubjectByIdView(APIView):
    permission_classes = [IsAdminUser]
   
    def get(self, request, *args, **kwargs):
        """Fetches a specific subject using the ID provided in the URL path."""
        subject_id = int(kwargs.get('id'))
       
        if not subject_id:
            return Response(
                {
                    'error': 'Subject not found'
                }, status=status.HTTP_404_NOT_FOUND
            )
        
        response = SubjectServices.get_subject_by_id(subject_id)
        serializer = ListSubjectSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
class SubjectByNameView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        """Filters subjects by name parameter passed through the URL."""
        subject_name = str(kwargs.get('name'))
        
        if not subject_name:
            return Response(
                {
                    'error': 'Subject name not found'
                }, status=status.HTTP_404_NOT_FOUND
            )
        
        response = SubjectServices.get_subject_name(subject_name)
        serializer = ListSubjectSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
class CreateSubjectView(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        """Handles the creation of a subject after validating the presence of an Institution ID."""
        data = request.data
        
        if not data or not 'institution_id' in data:
            return Response(
                {
                    'error': 'No data avaible or institution ID not found'
                }, status=status.HTTP_404_NOT_FOUND
            )
        
        try:
            response = SubjectServices.create_subject(data, data['institution_id'])
            serializer = ListSubjectSerializer(response)
            
            return Response(
                {
                    'message': 'The subject has been created successfully.',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateSubjectView(APIView):
    permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        """Updates an existing subject record ensuring both subject and institution IDs are valid."""
        data = request.data
        subject_id = int(kwargs.get('id'))
        
        if not data or not 'institution_id' in data or not subject_id:
            return Response(
                {
                    'error': 'No data avaible or institution ID not found or subject ID not found'
                }, status=status.HTTP_404_NOT_FOUND
            )
            
        try:
            response = SubjectServices.update_subject(
                data,
                subject_id,
                data['institution_id']
            )
            
            serializer = ListSubjectSerializer(response)
            
            return Response(
                {
                    'message': 'The subject has been updated successfully.',
                    'data': serializer.data
                }, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)