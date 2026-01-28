"""
This module implements the API endpoints for the Academic entity using Django Rest Framework's APIView.
The architecture follows a strict Separation of Concerns (SoC) principle where:
1. The View Layer: Intercepts HTTP requests (GET, POST, PUT), extracts parameters from the URL or body, 
   and delegates all business logic to the Service Layer.
2. The Service Layer (e.g., SubjectServices, AssistanceServices): Orchestrates data validation 
   and coordinates with the Repository for database persistence.
3. The Serialization Layer (e.g., ListSubjectSerializer): Transforms complex Django model instances 
   into native Python data types that can be easily rendered into JSON for the client.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from academic.services.subject import SubjectServices
from academic.serializers import ListSubjectSerializer

from academic.services.modality_assistance import ModalityAssistanceServices
from academic.services.assistance import AssistanceServices
from academic.services.disciplinary_action import DisciplinaryActionServices

from academic.serializers import (
    ListModalityAssistanceSerializer,
    ListAssistanceSerializer,
    ListDisciplinaryActionSerializer
)

# subject views

class ListSubjectView(APIView):
    permission_classes = [IsAuthenticated]
   
    def get(self, request):
        subject = SubjectServices.get_all_subject()
       
        if not subject:
            return Response({'error': 'List subject not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListSubjectSerializer(subject, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
class SubjectByIdView(APIView):
    permission_classes = [IsAdminUser]
   
    def get(self, request, *args, **kwargs):
        subject_id = int(kwargs.get('id'))
       
        if not subject_id:
            return Response({'error': 'Subject not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = SubjectServices.get_subject_by_id(subject_id)
        serializer = ListSubjectSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
class SubjectByNameView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        subject_name = str(kwargs.get('name'))
        
        if not subject_name:
            return Response({'error': 'Subject name not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = SubjectServices.get_subject_name(subject_name)
        serializer = ListSubjectSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
class CreateSubjectView(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        data = request.data
        
        if not data or not 'institution_id' in data:
            return Response({'error': 'No data avaible or institution ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            response = SubjectServices.create_subject(data, data['institution_id'])
            serializer = ListSubjectSerializer(response)
            
            return Response({
                'message': 'The subject has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateSubjectView(APIView):
    permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        subject_id = int(kwargs.get('id'))
        
        if not data or not 'institution_id' in data or not subject_id:
            return Response({'error': 'No data avaible or institution ID not found or subject ID not found'}, status=status.HTTP_404_NOT_FOUND)
            
        try:
            response = SubjectServices.update_subject(data, subject_id, data['institution_id'])
            serializer = ListSubjectSerializer(response)
            
            return Response({
                'message': 'The subject has been updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# modality assistance views

class CreateModalityAssistanceView(APIView):
    def post(self, request):
        data = request.data
        if not data:
            return Response({'message': 'No data avaible'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            response = ModalityAssistanceServices.create_modality_assitance(data)
            serializer = ListModalityAssistanceSerializer(response)
            return Response({
                'message': 'The modality assistance has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# assistance views

class ListAssistanceView(APIView):
    def get(self, request):
        assistance = AssistanceServices.get_all_assistance()
        
        if not assistance:
            return Response({'error': 'List assistance not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListAssistanceSerializer(assistance, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class AssistanceByStudentView(APIView):
    def get(self, request, *args, **kwargs):
        student = int(kwargs.get('id'))
        
        if not student:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = AssistanceServices.get_assistance_by_student(student)
        serializer = ListAssistanceSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
class AssistanceByDateView(APIView):
    def get(self, request, *args, **kwargs):
        date = kwargs.get('date')
        
        if not date:
            return Response({'error': 'Date not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = AssistanceServices.get_assistance_by_date(date)
        serializer = ListAssistanceSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
class CreateAssistanceView(APIView):
    def post(self, request):
        data = request.data
        
        if not data or 'modality_id' not in data or 'student_id' not in data:
            return Response({'message': 'No data avaible or modality ID not found or student ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            response = AssistanceServices.create_assistance(data, data['modality_id'], data['student_id'])
            serializer = ListAssistanceSerializer(response)
            
            return Response({
                'message': 'The assistance has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UpdateAssistanceView(APIView):
    def put(self, request, *args, **kwargs):
        data = request.data
        assistance = int(kwargs.get('id'))
        
        if not data or 'modality_id' not in data or 'student_id' not in data or not assistance:
            return Response({'message': 'No data avaible or modality ID not found or student ID not found or assistance ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            response = AssistanceServices.update_assistance(data, assistance, data['modality_id'], data['student_id'])
            serializer = ListAssistanceSerializer(response)
            
            return Response({
                'message': 'The assistance has been updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# disciplinary action views

class ListDisciplinaryActionView(APIView):
    def get(self, request):
        disciplinary_action = DisciplinaryActionServices.get_all_disciplinary_action()
        
        if not disciplinary_action:
            return Response({'error': 'List disciplinary action not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListDisciplinaryActionSerializer(disciplinary_action, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
class DisciplinaryActionByDateView(APIView):
    def get(self, request, *args, **kwargs):
        date = kwargs.get('date')
        
        if not date:
            return Response({'error': 'Date not found'}, status=status.HTTP_404_NOT_FOUND )
        
        response = DisciplinaryActionServices.get_disciplinary_action_by_date(date)
        serializer = ListDisciplinaryActionSerializer(response, many=True)
        return Response({'date': serializer.data}, status=status.HTTP_200_OK)

class DisciplinaryActionByStudentView(APIView):
    def get(self, request, *args, **kwargs):
        student = str(kwargs.get('name'))
        
        if not student:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = DisciplinaryActionServices.get_disciplinary_action_by_student(student)
        serializer = ListDisciplinaryActionSerializer(response)
        return Response({'date': serializer.data}, status=status.HTTP_200_OK)

class CreateDisciplinaryActionView(APIView):
    def post(self, request):
        data = request.data
        
        if not data or 'student_id' not in data:
            return Response({'message': 'No data avaible or student ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            response = DisciplinaryActionServices.create_disciplinary_action(data, data['student_id'])
            serializer = ListDisciplinaryActionSerializer(response)
            
            return Response({
                'message': 'The disciplinary action has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateDisciplinaryActionView(APIView):
    def put(self, request, *args, **kwargs):
        data = request.data
        disciplinaty_action = int(kwargs.get('id'))
        
        if not data or 'student_id' not in data or not disciplinaty_action:
            return Response({'message': 'No data avaible or student ID not found or disciplinary action ID not found'}, status=status.HTTP_404_NOT_FOUND)
            
        try:
            response = DisciplinaryActionServices.update_disciplanry_action(data, disciplinaty_action, data['student_id'])
            serializer = ListDisciplinaryActionSerializer(response)
            
            return Response({
                'message': 'The disciplinary action has been updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)