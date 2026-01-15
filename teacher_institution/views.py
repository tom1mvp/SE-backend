from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from teacher_institution.services.teaching_file import TeachingFileServices
from teacher_institution.services.teaching_assistance import TeachingAssistanceServices
from teacher_institution.services.teacher import TeacherServices


from teacher_institution.serializers import (
    ListTeachingFileSerializer,
    ListTeachingAssistanceSerializer,
    ListTeacherSerializer
)

"""
    Teacher Institution Management API Views
    
    This module serves as the primary interface for managing professional teaching files, 
    staff daily assistance records, and the core teacher profiles.
    
    It facilitates institutional administration by coordinating data flow between 
    web requests and specialized services, ensuring that professional records 
    and attendance are handled with high precision.
"""

# Views teaching file

# Retrieve the complete list of professional teaching files
class ListTeachingFileView(APIView):
   permission_classes = [IsAdminUser]
   
   def get(self, request):
       file = TeachingFileServices.get_all_teaching_file()
       
       if not file:
           return Response({'error': 'Teaching file list not found'}, status=status.HTTP_404_NOT_FOUND)
           
       serializer = ListTeachingFileSerializer(file, many=True)
       
       # Returns serialized data of all employment records within the institution
       return Response({'data': serializer.data}, status=status.HTTP_200_OK)
   
# Fetch a specific professional file by its unique internal ID
class TeachingFileByIdView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        file_id = int(kwargs.get('id'))
        
        if not file_id:
            return Response({'error': 'Teaching file not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = TeachingFileServices.get_teaching_file_by_id(file_id)
        
        serializer = ListTeachingFileSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

# Search for a professional record using the public-facing administrative number
class TeachingFileByNumberView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        file_number = int(kwargs.get('number'))
        
        if not file_number:
            return Response({'error': 'Teaching file number not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = TeachingFileServices.get_teaching_file_by_number(file_number)
        
        serializer = ListTeachingFileSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
# Handle the registration of new professional files into the system
class CreateTeachingFileView(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        data = request.data
        
        if not data:
            return Response({'error': 'No data avaible'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            # Coordinates the creation of an administrative file for future teacher assignment
            response = TeachingFileServices.create_teaching_file(data)
            
            serializer = ListTeachingFileSerializer(response)
        
            return Response({'message': 'The teaching file has been created successfully.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# Manage updates for existing professional records
class UpdateTeachingFileView(APIView):
    permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        
        file_id = int(kwargs.get('id'))
        
        if not data or not file_id:
            return Response({'error': 'No data avaible or Teaching file ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            # Commits updates to license numbers or admission dates
            response = TeachingFileServices.update_teaching_file(data, file_id)
            
            serializer = ListTeachingFileSerializer(response)
            
            return Response({'message': 'The teaching file has been updated successfully.', 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# Views teaching assistance

# Access the complete history of teacher attendance logs
class ListTeachingAssistanceView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, resquest):
        assistance = TeachingAssistanceServices.get_all_teaching_assistance()
        
        if not assistance:
            return Response({'error': 'Teaching assistance list not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListTeachingAssistanceSerializer(assistance, many=True)
        
        # Provides institutional oversight of staff presence and absences
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
# Retrieve a single assistance entry for granular record review
class TeachingAssistanceByIdView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        assistance_id = int(kwargs.get('id'))
        
        if not assistance_id:
            return Response({'error': 'Teaching assistance not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = TeachingAssistanceServices.get_teaching_assistance_by_id(assistance_id)
        
        serializer = ListTeachingAssistanceSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
# Filter attendance history by teacher name using relational lookups
class TeachingAssistanceByNameView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        assistance_name = str(kwargs.get('name'))
        
        if not assistance_name:
            return Response({'error': 'Teaching assistance name not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = TeachingAssistanceServices.get_teaching_assistance_by_name(assistance_name)
        
        serializer = ListTeachingAssistanceSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
# Monitor staff presence on a specific calendar date
class TeachingAssistanceByDateView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        assistance_date = kwargs.get('date')
        
        if not assistance_date:
            return Response({'error': 'Date not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = TeachingAssistanceServices.get_teaching_assistance_by_date(assistance_date)
        
        serializer = ListTeachingAssistanceSerializer(response, many=True)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

# Process the onboarding of new attendance entries
class CreateTeachingAssistanceView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    
    def post(self, request):
        data = request.data
        
        if not data or 'teacher_id' not in data:
            return Response({'error': 'No data avaible or teacher ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            # Validates and saves the assistance log for a specific staff member
            response = TeachingAssistanceServices.create_teaching_assistance(data, data['teacher_id'])
            
            serializer = ListTeachingAssistanceSerializer(response)
            
            return Response({'message': 'The teaching assistance has been created successfully.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# Modify existing attendance data, reasons, or observations
class UpdateTeachingAssistanceView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        
        assistance_id = int(kwargs.get('id'))
        
        if not data or 'teacher_id' not in data or not assistance_id:
            return Response({'error': 'No data avaible or teacher ID not found or assitance ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            response = TeachingAssistanceServices.update_teaching_assistance(data, assistance_id, data['teacher_id'])
            
            serializer = ListTeachingAssistanceSerializer(response)
            
            return Response({'message': 'The teaching assistance has been updated successfully.', 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# View teacher

# List all core teacher profiles linking identity and employment records
class ListTeacherView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        teacher = TeacherServices.get_all_teacher()
        
        if not teacher:
            return Response({'error': 'Teacher list not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListTeacherSerializer(teacher, many=True)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
# Fetch a definitive teacher profile by their system ID
class TeacherByIdView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        teacher_id = int(kwargs.get('id'))
        
        if not teacher_id:
            return Response({'error': 'Teachr not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = TeacherServices.get_teacher_by_id(teacher_id)
        
        serializer = ListTeacherSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

# Search for teachers by their first name across the institutional directory
class TeacherByNameView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        teacher_name = str(kwargs.get('name'))
        
        if not teacher_name:
            return Response({'error': 'Teacher name not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = TeacherServices.get_teacher_by_name(teacher_name)
        
        serializer = ListTeacherSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

# Coordinate the creation of a Teacher profile by linking a Person with a File
class CreateTeacherView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        
        if not data or 'file_id' not in data or 'person_id' not in data:
            return Response({'error': 'No data avaible or file ID not found or person ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            # Establishes the core relationship between human identity and administrative record
            response = TeacherServices.create_teacher(data, data['person_id'], data['file_id'])
            
            serializer = ListTeacherSerializer(response)
            
            return Response({'message': 'The teacher has been created successfully.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)