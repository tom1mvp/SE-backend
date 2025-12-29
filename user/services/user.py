from django.contrib.auth.hashers import make_password, check_password


from rest_framework.exceptions import ValidationError


from user.repositories.user import UserRepository
from user.serializers import ListUserSerializer


class UserService:
    """
    User Management Service

    Orchestrates business logic for user-related operations. 
    Acts as a mediator between the API controllers and the UserRepository, 
    ensuring data integrity, password hashing, and business rule validation.

    Business Logic Handled:
    - User Registration: Processes raw data and hashes passwords before storage.
    - Identity Management: Validates unique constraints (username).
    - Status Transitions: Controls the logic for deactivating and recovering accounts.
    - Role Validation: Ensures users are assigned valid system permissions.
    """
    
    @staticmethod
    def get_all_user():
        # Returns all users in the database
        return UserRepository.get_all_user()
    
    @staticmethod
    def get_user_by_id(user_id):
        # Returns users by their ID
        return UserRepository.get_user_by_id(user_id)
    
    @staticmethod
    def get_user_by_username(username):
        # Returns users by their username
        return UserRepository.get_user_by_username(username)
    
    @staticmethod
    def get_user_by_role(role):
        # Returns users by their role
        return UserRepository.get_user_by_role(role)
    
     # Method POST (login and register)
    
    # Password hash
    @staticmethod
    def encrip_password(data):
        data['password'] = make_password(data.get('password'))
        
        # Hash
        serializer = ListUserSerializer(data=data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            return user
        else:
            raise ValidationError(serializer.errors)
        
    @staticmethod
    def login(data):
        user = UserRepository.get_user_by_username(data['username'])
        
        # Verify if user exist
        if not user:
            raise ValidationError('Error: ', 'User does not exist')
        
        if not check_password(data['password'], user.password):
            raise ValidationError({'error': 'Incorrect password'})
        
        # Return user info
        return {
            'id': user.id,
            'username': user.username,
            'image': user.image,
            'role': user.role,
            'is_active': user.is_active
        }
    
    @staticmethod
    def register(data):
        # Check if the user name already exist
        if UserRepository.get_user_by_username(data['username']):
            return {'error': 'User already exists.'}
        
        confirm_password = data['confirm_password']
        password = data['password']
        
        
        # verify that the password matches the confirm password field
        if password != confirm_password:
            return {'error': 'Passwords do not match'}
        
        # Hash password
        hashed_password = make_password(data['password'])
        
        # Create user
        user = UserRepository.create_user(
            username=data['username'],
            password=hashed_password,
            image=data['image'],
            role=data['role']
        )
        
        return user
    
    @staticmethod
    def update_user(data, user_id):
        required_fields = ['username', 'password', 'image', 'role']
        
        # Verify that all required fields in the form have been filled in.
        for field in required_fields:
            if field not in data:
                raise ValidationError({field: f'El campo {field} es obligatorio'})
        
        # Hash password
        hashed_password = make_password(data['password'])
        
        # Update user
        user = UserRepository.update_user(
            user_id=user_id,
            username=data['username'],
            password=hashed_password,
            role=data['role'],
            image=data['image']
        )
        
        return user
    
    @staticmethod
    def delete_user(data, user_id):
        # Perform a soft delete by deactivating the user account.
        return UserRepository.delete_user(user_id)
    
    @staticmethod
    def recover_user(user_id):
        # Restore a soft-deleted user by reactivating their account.
        return UserRepository.recover_user(user_id)