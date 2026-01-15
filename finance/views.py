from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from finance.services.salary import TeacherSalaryServices
from finance.serializers import ListTeacherSalarySerializer

"""
    Teacher Salary API Views
    
    This module manages the financial interface for teacher compensation, 
    handling payroll queries, salary creation, and record updates.
    
    It ensures financial data integrity by interfacing with the Salary Service 
    layer and providing structured serialized responses.
"""

# Retrieve the complete list of teacher salary records
class ListTeacherSalaryView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        # Accesses the service layer to pull all payroll history.
        salary = TeacherSalaryServices.get_all_salary()
        
        if not salary:
            return Response({'error': 'Salary list not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListTeacherSalarySerializer(salary, many=True)
        # Returns a collection of all financial transactions recorded.
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

# Fetch a specific salary record using its unique database identifier
class TeacherSalaryByIdView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        salary_id = int(kwargs.get('id'))
        
        if not salary_id:
            return Response({'error': 'Salary not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = TeacherSalaryServices.get_salary_by_id(salary_id)
        
        serializer = ListTeacherSalarySerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
# Filter salary records by a specific payment or issuance date
class TeacherSalaryByDateView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    def get(self, request, *args, **kwargs):
        date = kwargs.get('date')
        
        if not date:
            return Response({'error': 'Date not found'}, status=status.HTTP_404_NOT_FOUND)
        
        response = TeacherSalaryServices.get_salary_by_date(date)
        
        serializer = ListTeacherSalarySerializer(response, many=True)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
# Retrieve compensation details for a specific teacher via their ID
class TeacherSalaryByTeacherView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        teacher_id = int(kwargs.get('id'))
        
        if not teacher_id:
            return Response({'error': 'Teacher ID not foud'}, status=status.HTTP_404_NOT_FOUND)
        
        # Performs a lookup based on the teacher's professional profile relationship.
        response = TeacherSalaryServices.get_salary_by_teacher(teacher_id)
        
        serializer = ListTeacherSalarySerializer(response)
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    

# Handle the creation and persistence of new salary entries
class CreateTeacherSalaryView(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        data = request.data
        
        # Validates that the payroll data is linked to an existing professional file.
        if not data or 'file_id' not in data:
            return Response({'error': 'No data avaible or file ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            # Delegates the creation logic and financial validation to the service.
            response = TeacherSalaryServices.create_salary(
                data,
                data['file_id']
            )
            
            serializer = ListTeacherSalarySerializer(response)
            
            return Response({'message': 'The teacher salary has been created successfully.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# Manage updates to existing compensation records (Amount, Status, etc.)
class UpdateTeacherSalaryView(APIView):
    permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        
        salary_id = int(kwargs.get('id'))
        
        if not data or 'file_id' not in data or not salary_id:
            return Response({'error': 'No data avaible or file ID not found or salary ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            # Updates the financial record ensuring the salary ID remains consistent.
            response = TeacherSalaryServices.update_salary(
                data,
                salary_id # Corrected to pass the ID from the URL kwargs.
            )
            
            serializer = ListTeacherSalarySerializer(response)
            
            return Response({'message': 'The teacher salary has been updated successfully.', 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)