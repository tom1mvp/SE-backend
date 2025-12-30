from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from user.services.user import UserService

from user.serializers import ListUserSerializer

"""
    User Management API Views
    
    This module handles the HTTP interface for user-related operations, acting as 
    the entry point for the School Management System's user administration.
    
    It coordinates between the incoming web requests and the UserService,
    enforcing security via permission classes (IsAdminUser, IsAuthenticated)
    and formatting outgoing data through ListUserSerializer.
"""

# Retrieve the complete list of users (Admin Only)
class ListUserView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        user = UserService.get_all_user()
        if not user:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListUserSerializer(user, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

# Fetch a specific user profile by their ID (Admin Only)
class UserByIdView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        user_id = int(kwargs.get('id'))
        response = UserService.get_user_by_id(user_id)
        
        if not response:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = ListUserSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

# Search for a user by their unique username (Admin Only)
class UserByUsernameView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        username = str(kwargs.get('username'))
        response = UserService.get_user_by_username(username)
        
        if not response:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = ListUserSerializer(response)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

# Filter users by institutional role: Student, Teacher, etc. (Admin Only)
class UserByRoleView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        role = str(kwargs.get('role'))
        response = UserService.get_user_by_role(role)
        
        if not response:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = ListUserSerializer(response, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

# Handle user authentication and credential validation
class LoginView(APIView):
    def post(self, request):
        data = request.data
        if 'username' not in data or 'password' not in data:
            return Response({"Error": "Required fields are missing"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            response = UserService.login(data) or {}
            return Response({'Message': 'Welcome, user', "data": response}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Manage the onboarding of new users into the system
class RegisterView(APIView):
    def post(self, request):
        data = request.data
        try:
            response = UserService.register(data)
            serializer = ListUserSerializer(response)
            return Response({
                'Message': 'Successfully registered user',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
# Update user profile information (Authenticated users only)
class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, *args, **kwargs):
        data = request.data
        user_id = int(kwargs.get('id'))
        
        try:
            response = UserService.update_user(data, user_id)
            serializer = ListUserSerializer(response)
            return Response({
                'Message': 'The user has been successfully updated',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
# Perform a logical deactivation (Soft Delete) of a user account
class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request, *args, **kwargs):
        user_id = int(kwargs.get('id'))
        try:
            UserService.delete_user(user_id)
            return Response({'message': 'The user was successfully deactivated.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Re-enable access for a previously deactivated account (Admin Only)
class RecoverUserView(APIView):
    permission_classes = [IsAdminUser]
    
    def patch(self, request, *args, **kwargs):
        user_id = int(kwargs.get('id'))
        try:
            UserService.recover_user(user_id)
            return Response({'message': 'The user was successfully recovered.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)