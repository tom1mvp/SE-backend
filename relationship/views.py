from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from relationship.services.relationship import RelationshipServices
from relationship.serializers import ListRelationshipSerializer

class ListRelationshipView(APIView):
    """
    View to list all student-tutor relationships.
    """
    permission_classes = [IsAdminUser]
    def get(self, request):
        # Fetches all relationships from the service layer.
        relationship = RelationshipServices.get_all_relationship()
        
        if not relationship:
            return Response({
                'error': 'List relationship not found'
            }, status=status.HTTP_404_NOT_FOUND)
            
        # Serializes the queryset into JSON data.
        serializer = ListRelationshipSerializer(relationship, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class RelationshipByKinshipView(APIView):
    """
    View to filter relationships by kinship type (e.g., Father, Mother).
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
   
    def get(self, request, *args, **kwargs):
        kinship = str(kwargs.get('kinship'))
       
        if not kinship:
            return Response({
                'error': 'Kinship name not found'
            }, status=status.HTTP_404_NOT_FOUND)
           
        # Retrieves filtered data based on the kinship parameter.
        response = RelationshipServices.get_relationship_by_kinship(kinship)
        serializer = ListRelationshipSerializer(response, many=True)
       
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
   
class RelatioshipByTutorView(APIView):
    """
    View to retrieve relationships associated with a specific tutor's name.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        name = str(kwargs.get('name'))
        
        if not name:
            return Response({
                'error': 'Tutor name not found'
            }, status=status.HTTP_404_NOT_FOUND)
            
        # Fetches a single relationship instance by tutor name.
        response = RelationshipServices.get_relationship_by_tutor(name)
        serializer = ListRelationshipSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class CreateRelationshipView(APIView):
    """
    View to handle the creation of a new relationship record.
    """
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        
        # Validates that necessary IDs are present in the request body.
        if not data or 'tutor_id' not in data or 'student_id' not in data:
            return Response({
                'error': 'No data available or IDs missing'
            }, status=status.HTTP_404_NOT_FOUND)
        
        try:
            # Orchestrates relationship creation via the service.
            response = RelationshipServices.create_relationship(data, data['tutor_id'], data['student_id'])
            serializer = ListRelationshipSerializer(response)
            
            return Response({
                'message': 'The relationship has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateRelationshipView(APIView):
    """
    View to update existing relationship details.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        relationship_id = int(kwargs.get('id'))
        
        # FIXED: Changed 'relationship_id' to 'not relationship_id'
        if not data or 'tutor_id' not in data or 'student_id' not in data or not relationship_id:
            return Response({
                'error': 'No data available or missing mandatory IDs'
            }, status=status.HTTP_404_NOT_FOUND)
            
        try:
            # Updates the record and returns the new state.
            response = RelationshipServices.update_relationship(data, relationship_id, data['tutor_id'], data['student_id'])
            serializer = ListRelationshipSerializer(response)
            
            return Response({
                'message': 'The relationship has been updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteRelationshipView(APIView):
    """
    View to perform logical deletion (deactivation) of a relationship.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def patch(self, request, *args, **kwargs):
        relationship_id = int(kwargs.get('id'))
        
        if not relationship_id:
            return Response({
                'error': 'relationship ID not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        try:
            RelationshipServices.delete_relationship(relationship_id)
            return Response({'message': 'The relationship was successfully deactivated.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class RecoverRelationshipView(APIView):
    """
    View to restore a previously deactivated relationship.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def patch(self, request, *args, **kwargs):
        relationship_id = int(kwargs.get('id'))
        
        if not relationship_id:
            return Response({
                'error': 'relationship ID not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        try:
            RelationshipServices.recover_relationship(relationship_id)
            return Response({'message': 'The relationship was successfully recovered.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)