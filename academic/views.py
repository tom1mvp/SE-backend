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
from academic.services.course import CourseServices

from academic.serializers import (
    ListModalityAssistanceSerializer,
    ListAssistanceSerializer,
    ListDisciplinaryActionSerializer,
    ListCourseSerializer
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
        
class SubjectByNameView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
   
    def get(self, request, *args, **kwargs):
        subject_name = str(kwargs.get('name'))
       
        if not subject_name:
            return Response({'error': 'Subject name not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = SubjectServices.get_subject_by_name(subject_name)
        serializer = ListSubjectSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class SubjectByCourseView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        course_name = str(kwargs.get('name'))
        
        if not course_name:
            return Response({'error': 'Course name not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = SubjectServices.get_subject_by_course(course_name)
        serializer = ListSubjectSerializer(response, many=True)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
class CreateSubjectView(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        data = request.data
        
        if not data or not 'course_id' in data or not 'teacher_id' in data:
            return Response({'error': 'No data avaible or course ID not found or teacher ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            response = SubjectServices.create_subject(data, data['course_id'], data['teacher_id'])
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
        
        if not data or not 'course_id' in data or not 'teacher_id' in data or not subject_id:
            return Response({'error': 'No data avaible or course ID not found or teacher ID not found or subject ID not found'}, status=status.HTTP_404_NOT_FOUND)
            
        try:
            response = SubjectServices.update_subject(data, subject_id, data['course_id'], data['teacher_id'])
            serializer = ListSubjectSerializer(response)
            
            return Response({
                'message': 'The subject has been updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteSubjectView(APIView):
    permission_classes = [IsAdminUser]
    
    def patch(self, reques, *args, **kwargs):
        subject_id = int(kwargs.get('id'))
        
        if not subject_id:
            return Response({'error': 'subject ID not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            SubjectServices.delete_subject(subject_id)
            return Response({'message': 'The subject was successfully deactivated.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RecoverSubjectView(APIView):
    permission_classes = [IsAdminUser]
    
    def patch(self, reques, *args, **kwargs):
        subject_id = int(kwargs.get('id'))
        
        if not subject_id:
            return Response({'error': 'subject ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            SubjectServices.recover_subject(subject_id)
            return Response({'message': 'The subject was successfully recovered.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# modality assistance views
class ListModalityAssistanceView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        modality_assistance = ModalityAssistanceServices.get_all_modality_assitance()
        
        if not modality_assistance:
            return Response({'error': 'List modality assistance not found'})
        
        serializer = ListModalityAssistanceSerializer(modality_assistance, many=True)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
    
class CreateModalityAssistanceView(APIView):
    permission_classes = [IsAdminUser]
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
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request, *args, **kwargs):
        student = int(kwargs.get('id'))
        
        if not student:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = AssistanceServices.get_assistance_by_student(student)
        serializer = ListAssistanceSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
class AssistanceByDateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request, *args, **kwargs):
        date = kwargs.get('date')
        
        if not date:
            return Response({'error': 'Date not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = AssistanceServices.get_assistance_by_date(date)
        serializer = ListAssistanceSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
class CreateAssistanceView(APIView):
    permission_classes = [IsAdminUser]
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
    permission_classes = [IsAdminUser]
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
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request, *args, **kwargs):
        date = kwargs.get('date')
        
        if not date:
            return Response({'error': 'Date not found'}, status=status.HTTP_404_NOT_FOUND )
        
        response = DisciplinaryActionServices.get_disciplinary_action_by_date(date)
        serializer = ListDisciplinaryActionSerializer(response, many=True)
        return Response({'date': serializer.data}, status=status.HTTP_200_OK)

class DisciplinaryActionByStudentView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request, *args, **kwargs):
        student = str(kwargs.get('name'))
        
        if not student:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = DisciplinaryActionServices.get_disciplinary_action_by_student(student)
        serializer = ListDisciplinaryActionSerializer(response)
        return Response({'date': serializer.data}, status=status.HTTP_200_OK)

class CreateDisciplinaryActionView(APIView):
    permission_classes = [IsAdminUser]
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
    permission_classes = [IsAdminUser]
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
        
# course views

class ListCourseView(APIView):
   # permission_classes = [IsAdminUser, IsAuthenticated]
   
   def get(self, request):
       course = CourseServices.get_all_course()
       
       if not course:
           return Response({
               'error': 'List course not found'
           }, status=status.HTTP_404_NOT_FOUND)
           
       serializer = ListCourseSerializer(course, many=True)
       
       return Response({'data': serializer.data}, status=status.HTTP_200_OK)
   
class CourseByNameView(APIView):
    # permission_classes = [IsAdminUser, IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        name = str(kwargs.get('name'))
        
        if not name:
            return Response({
                'error': 'Course name not found'
            }, status=status.HTTP_404_NOT_FOUND)
            
        response = CourseServices.get_course_by_name(name)
        
        serializer = ListCourseSerializer(response, many=True)
       
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class CourseByInstitutionView(APIView):
    # permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        name = str(kwargs.get('name'))
        
        if not name:
            return Response({
                'error': 'Institution name not found'
            }, status=status.HTTP_404_NOT_FOUND)
            
        response = CourseServices.get_course_by_institution(name)
        
        serializer = ListCourseSerializer(response, many=True)
       
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class CreateCourseView(APIView):
    # permission_classes = [IsAdminUser]
    
    def post(self, request):
        data = request.data
        
        if not data or 'institution_id' not in data:
            return Response({
                'error': 'No data avaible or institution ID not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        try:
            response = CourseServices.create_course(data, data['institution_id'])
            
            serializer = ListCourseSerializer(response)
            
            return Response({
                'message': 'The course has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UpdateCourseView(APIView):
    # permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        
        course_id = int(kwargs.get('id'))
        
        if not data or 'institution_id' not in data or not course_id:
            return Response({
                'error': 'No data avaible or institution ID not found or course ID not found'
            }, status=status.HTTP_404_NOT_FOUND)
            
        try:
            response = CourseServices.update_course(data, course_id, data['institution_id'])
            
            serializer = ListCourseSerializer(response)
            
            return Response({
                'message': 'The course has been updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            