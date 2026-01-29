from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from grades.services.assessment_category import AssessmentCategoryServices
from grades.services.grades import GradeServices
from grades.serializers import ListGradeSerializer, ListAssessmentCategorySerializer 


"""
    Assessment Category Views
    
    This section handles the HTTP request/response cycle for grading categories.
    It translates API calls into service operations and formats the resulting
    data using specialized serializers.
"""

class ListAssessmentCategoryView(APIView):
    permission_classes = [IsAdminUser]
    # Provides a list of all available assessment categories.
    def get(self, request):
        assessment_category = AssessmentCategoryServices.get_all_assessment_category()
        
        if not assessment_category:
            return Response({'error': 'No assessment categories found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListAssessmentCategorySerializer(assessment_category, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class CreateAssessmentCategoryView(APIView):
    permission_classes = [IsAdminUser]
    # Handles the creation of new assessment categories through a POST request.
    def post(self, request):
        data = request.data
        if not data:
            return Response({'error': 'No data provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            response = AssessmentCategoryServices.create_assessment_category(data)
            serializer = ListAssessmentCategorySerializer(response)
            return Response({
                'message': 'The assessment category has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


"""
    Grades Views
    
    This section manages the endpoint logic for student grades.
    It includes operations for listing, filtering by subject or term,
    creating, and updating academic performance records.
"""

class ListGradesView(APIView):
    permission_classes = [IsAuthenticated]
    # Retrieves a comprehensive list of all student grades.
    def get(self, request):
        grades = GradeServices.get_all_grades()
        if not grades:
            return Response({'error': 'No grades found'}, status=status.HTTP_404_NOT_FOUND)
           
        serializer = ListGradeSerializer(grades, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class GradesBySubjectView(APIView):
    permission_classes = [IsAuthenticated]
    # Filters and retrieves grades based on the subject name provided in the URL.
    def get(self, request, *args, **kwargs):
        name = kwargs.get('name')
        if not name:
            return Response({'error': 'Subject name parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)
            
        response = GradeServices.get_grade_by_subject(name)
        # many=True is required because one subject usually has multiple grades.
        serializer = ListGradeSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
class GradesByTermView(APIView):
    permission_classes = [IsAuthenticated]
    # Filters and retrieves grades based on the academic term provided in the URL.
    def get(self, request, *args, **kwargs):
        term = kwargs.get('term')
        if not term:
            return Response({'error': 'Term parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)
            
        response = GradeServices.get_grade_by_term(term)
        # many=True is required because one term contains multiple grades.
        serializer = ListGradeSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class GradesByStudentView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request, *args, **kwargs):
        student = str(kwargs.get('name'))
        
        if not student:
            return Response({'error': 'Student parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)
        
        response = GradeServices.get_grade_by_student(student)
        
        serializer = ListGradeSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class CreateGradesView(APIView):
    permission_classes = [IsAuthenticated]
    # Creates a new grade record, ensuring all relational IDs are present in the request.
    def post(self, request):
        data = request.data
        required_ids = ['subject_id', 'student_id', 'category_id']
        
        if not data or not all(k in data for k in required_ids):
            return Response({
                'error': 'Missing data or required relational IDs (subject, student, category)'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            response = GradeServices.create_grade(data, data['subject_id'], data['student_id'], data['category_id'])
            serializer = ListGradeSerializer(response)
            return Response({
                'message': 'The grade has been created successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateGradesView(APIView):
    permission_classes = [IsAuthenticated]
    # Updates an existing grade record identified by ID.
    def put(self, request, *args, **kwargs):
        data = request.data
        grade_id = kwargs.get('id')
        required_ids = ['subject_id', 'student_id', 'category_id']
        
        if not data or not grade_id or not all(k in data for k in required_ids):
            return Response({
                'error': 'Missing payload data or grade identification'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            response = GradeServices.update_grade(data, grade_id, data['subject_id'], data['student_id'], data['category_id'])
            serializer = ListGradeSerializer(response)
            return Response({
                'message': 'The grade has been updated successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)