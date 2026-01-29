from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from tutor_institution.services.tutor import TutorServices
from tutor_institution.serializers import ListTutorSerializer


class ListTutorView(APIView):
    
    """
    API View to retrieve a complete list of all tutors registered in the system.
    This endpoint calls the service layer to fetch all records and returns them 
    serialized in a list format.
    """
    permission_classes = [IsAdminUser]
   
    def get(self, request):
        # Fetching all tutor instances through the Service layer
        tutor = TutorServices.get_all_tutor()
       
        if not tutor:
            return Response({'error': 'Tutor list not found'}, status=status.HTTP_404_NOT_FOUND)
       
        # Serializing the queryset with many=True since it returns multiple objects
        serializer = ListTutorSerializer(tutor, many=True)
       
        # Note: Added .data to the serializer to return the actual JSON representation
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
   

class TutorByIdView(APIView):
    """
    API View to retrieve a single tutor's information based on their unique ID.
    The ID is extracted from the URL parameters and validated before processing.
    """
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Extracting the ID from the URL keyword arguments
        tutor_id = int(kwargs.get('id'))
        
        if not tutor_id:
            return Response({
                'error': 'Tutor ID parameter is missing'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Requesting specific tutor data from the Service layer
        response = TutorServices.get_tutor_by_id(tutor_id)
        
        if not response:
            return Response({'error': 'Tutor not found'}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = ListTutorSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class TutorByNameView(APIView):
    """
    API View that allows searching for tutors by the first name of the associated person.
    This enables dynamic searches for specific staff or family members in the database.
    """
    permission_classes = [IsAdminUser, IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        # Extracting the name string from the URL
        tutor_name = str(kwargs.get('name'))
        
        if not tutor_name:
            return Response({
                'error': 'Person name parameter is missing'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        # Calling the service to perform a case-insensitive search
        response = TutorServices.get_tutor_by_name(tutor_name)
        
        serializer = ListTutorSerializer(response, many=True)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class CreateTutorView(APIView):
    """
    API View to handle the creation of new Tutor records via POST requests.
    It validates the incoming payload and handles potential errors during the 
    persistence process.
    """
   
    def post(self, request):
        data = request.data
       
        # Basic validation to ensure the required person_id is present in the request
        if not data or 'person_id' not in data:
            return Response({
                'error': 'No data available or person ID not found'
            }, status=status.HTTP_400_BAD_REQUEST)
           
        try:
            # Invoking the service to handle business logic and repository calls
            response = TutorServices.create_tutor(data, data['person_id'])

            serializer = ListTutorSerializer(response)
            
            # Returning the successfully created object with a 201 Created status
            return Response(
                {
                    'message': 'The tutor has been created successfully.',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            # Capturing business logic errors (like Person not found) and returning them to the client
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)