from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from student_institution.services.allergy import AllergyServices
from student_institution.services.subject_erollment import SubjectEnrollmentServices
from student_institution.services.student import StudentServices
from student_institution.services.student_file import StudentFileServices


from student_institution.serializers import (
    ListAllergyKindSerializer,
    ListSubjectEnrollmentSerializer,
    ListStudentSerializer,
    ListStudentFileSerializer
)

"""
Allergy-related API Views.
Handles listing, retrieving, creating, and updating allergy types.
"""

class ListAllergyView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        allergy = AllergyServices.get_all_allergy()
        
        if not allergy:
            return Response({'Error': 'Allergy list not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the queryset and return data
        serializer = ListAllergyKindSerializer(allergy, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    
class AllergyByIdView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        allergy_id = int(kwargs.get('id'))
        
        if not allergy_id:
            return Response({'Error': 'Allergy not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = AllergyServices.get_allergy_by_id(allergy_id)
        serializer = ListAllergyKindSerializer(response)
        
        # Note: Standard success status 200_OK
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    
class AllergyByNameView(APIView):
    
    def get(self, request, *args, **kwargs):
        allergy_name = str(kwargs.get('name'))
        
        if not allergy_name:
            return Response({'Error': 'Allergy name not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = AllergyServices.get_allergy_by_name(allergy_name)
        serializer = ListAllergyKindSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class CreateAllergyView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    
    def post(self, request):
        data = request.data
        
        try:
            if not data:
                return Response({'error': 'No data avaible'}, status=status.HTTP_400_BAD_REQUEST)
        
            response = AllergyServices.create_allergy(data)
            serializer = ListAllergyKindSerializer(response)
        
            return Response(
                {
                    'message': 'The allergy has been created successfully.',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
class UpdateAllergyView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        allergy_id = int(kwargs.get('id'))
        
        try:
            if not data or not allergy_id:
                return Response({'error': 'Not data is avaible or allergy_id not found'}, status=status.HTTP_404_NOT_FOUND)
        
            response = AllergyServices.update_allergy(data, allergy_id)
            serializer = ListAllergyKindSerializer(response)
        
            return Response(
                {
                    'message': 'The allergy has been updated successfully.',
                    'data': serializer.data
                }, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

"""
Student-related API Views.
Handles core student entity operations including logical deletion and recovery.
"""

class ListStudentView(APIView):
    def get(self, request):
        stundet = StudentServices.get_all_student()
        
        if not stundet:
            return Response({'error': 'Student list not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListStudentSerializer(stundet, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class StudentByIdView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        student_id = int(kwargs.get('id'))
        
        if not student_id:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = StudentServices.get_student_by_id(student_id)
        serializer = ListStudentSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
    
class StudentByNameView(APIView):
    def get(self, request, *args, **kwargs):
        student = str(kwargs.get('name'))
        
        if not student:
            return Response({'error': 'Student name not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = StudentServices.get_student_by_name(student)
        serializer = ListStudentSerializer(response, many=True)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

class CreateStudentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        
        try:
            # Check for core relationship IDs
            if not data or 'person_id' not in data or 'student_file_id' not in data:
                return Response({'error': 'Missing required foreign keys'}, status=status.HTTP_400_BAD_REQUEST)
            
            response = StudentServices.create_student(data, data['person_id'], data['student_file_id'])
            serializer = ListStudentSerializer(response)
            
            return Response(
                {
                    'message': 'The student has been created successfully.',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class DeleteStudentView(APIView):
    permisson_classes = [IsAuthenticated]
    
    def patch(self, request, *args, **kwargs):
        student_id = int(kwargs.get('id'))
        
        if not student_id:
            return Response({'error': 'ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            StudentServices.delete_student(student_id)
            return Response({'message': 'The student was successfully deactivated.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class RecoverStudentView(APIView):
    permisson_classes = [IsAdminUser]
    
    def patch(self, request, *args, **kwargs):
        student_id = int(kwargs.get('id'))
        
        if not student_id:
            return Response({'error': 'ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            StudentServices.recover_student(student_id)    
            return Response({'message': 'The student was successfully recovered.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

"""
Subject Enrollment API Views.
Manages the registration process for students in specific academic subjects and cycles.
"""

class ListSubjectErollmentView(APIView):
    permission_classes = [IsAuthenticated]
   
    def get(self, request):
        subject_erollment = SubjectEnrollmentServices.get_all_subject_enrollment()
       
        if not subject_erollment:
            return Response({'error': 'List subject enrollment not found'}, status=status.HTTP_404_NOT_FOUND)
           
        serializer = ListSubjectEnrollmentSerializer(subject_erollment, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class SubjectErollmentByIdView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        subject_erollment_id = int(kwargs.get('id'))
        
        if not subject_erollment_id:
            return Response({'error': 'Subject enrollment not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        response = SubjectEnrollmentServices.get_subject_enrollment_by_id(subject_erollment_id)
        serializer = ListSubjectEnrollmentSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class SubjectErollmentByElectiveCycleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        elective_cycle = int(kwargs.get('year'))
        
        if not elective_cycle:
            return Response({'error': 'Elective cycle not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = SubjectEnrollmentServices.get_subject_enrollment_by_elective_cycle(elective_cycle)
        serializer = ListSubjectEnrollmentSerializer(response, many=True)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class CreateSubjectErollmentView(APIView):
    permission_classes = [IsAdminUser]
   
    def post(self, request):
        data = request.data
       
        # Validation for composite relationship data
        if not data or 'student_id' not in data or 'subject_id' not in data or 'elective_cycle_id' not in data:
            return Response({'error': 'Missing required enrollment data'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            response = SubjectEnrollmentServices.create_subject_enrollment(
                data['student_id'], data['subject_id'], data['elective_cycle_id']
            )
            serializer = ListSubjectEnrollmentSerializer(response)
            
            return Response(
                {
                    'message': 'The subject enrollment has been created successfully.',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UpdateSubjectErollmentView(APIView):
    permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        subject_erollment_id = int(kwargs.get('id'))
        
        if not data or 'student_id' not in data or 'subject_id' not in data or 'elective_cycle_id' not in data or not subject_erollment_id:
            return Response({'error': 'Missing required IDs or data'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            response = SubjectEnrollmentServices.update_subject_enrollment(
                subject_erollment_id, data['student_id'], data['subject_id'], data['elective_cycle_id']
            )
            serializer = ListSubjectEnrollmentSerializer(response)
            
            return Response(
                {
                    'message': 'The subject enrollment has been updated successfully.',
                    'data': serializer.data
                }, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

"""
Student Administrative File API Views.
Manages the specific administrative records, including institutional links and medical data.
"""

class ListStudentFileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        student_file = StudentFileServices.get_all_student_file()
        
        if not student_file:
            return Response({'error': 'Student file list not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListStudentFileSerializer(student_file, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class StudentFileByIdView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        student_file_id = int(kwargs.get('id'))
        
        if not student_file_id:
            return Response({'error': 'Student file not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = StudentFileServices.get_student_file_by_id(student_file_id)
        serializer = ListStudentFileSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class StudentFileByNumberView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        number = str(kwargs.get('number'))
        
        if not number:
            return Response({'error': 'Number not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = StudentFileServices.get_student_file_by_number(number)
        serializer = ListStudentFileSerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class CreateStudentFileView(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        data = request.data
        
        if not data or 'allergy_id' not in data or 'institution_id' not in data:
            return Response({'error': 'Data is not avaible or institution ID not found or allergy ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            response = StudentFileServices.crear_student_file(data, data['institution_id'], data['allergy_id'])
            serializer = ListStudentFileSerializer(response)
            
            return Response(
                {
                    'message': 'The student file has been created successfully.',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UpdateStudentFileView(APIView):
    permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        student_file_id = int(kwargs.get('id'))
        
        if not data or 'allergy_id' not in data or 'institution_id' not in data or not student_file_id:
            return Response({'error': 'Missing IDs for update'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            response = StudentFileServices.update_student_file(data, student_file_id, data['institution_id'], data['allergy_id'])
            serializer = ListStudentFileSerializer(response)
            
            return Response(
                {
                    'message': 'The student file has been updated successfully.',
                    'data': serializer.data
                }, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DeleteStudentFileView(APIView):
    permission_classes = [IsAdminUser]
    
    def patch(self, request, *args, **kwargs):
        student_file_id = int(kwargs.get('id'))
        
        if not student_file_id:
            return Response({'error': 'ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            StudentFileServices.delete_student_file(student_file_id)
            return Response({'message': 'The file was successfully deactivated.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)