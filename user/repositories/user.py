from user.models import User


class UserRepository:

    """
        User Management Repository

        Handles all persistence logic for school system users. 
        Mainly used to provision new accounts and manage their lifecycle, 
        including account recovery and status management.

        Methods:
        - GET:
            * List all users.
            * Filter by username or role.
            * Retrieve a specific user by ID (Primary Key).
        - POST: Register/Create a new user in the database.
        - PUT: Perform a full update of user information.
        - PATCH:
            * Deactivate users via soft delete (archive).
            * Restore/Recover deactivated accounts (un-archive).
    """

    @staticmethod
    def get_all_user():
        # Retrieve all user records from the database, including inactive ones.
        return User.objects.all()
    
    @staticmethod
    def get_user_by_id(user_id):
        # Fetch a single user by their primary key (ID).
        return User.objects.filter(id=user_id).first()
    
    @staticmethod
    def get_user_by_username(username):
        # Find a specific user using their unique username.
        return User.objects.filter(username__icontains=username).first()
    
    @staticmethod
    def get_user_by_role(role):
        # Filter and return a list of users associated with a specific system role.
        return User.objects.filter(role__icontains=role).first()
    
    @staticmethod
    def create_user(
        username,
        password,
        role,
        image,
        is_active=True
    ):
        # Persist a new user record into the database.
        new_user = User.objects.create(
            username=username,
            password=password,
            role=role,
            image=image,
            is_active=is_active
        )
        
        return new_user
    
    # Perform a full update of an existing user's information.
    @staticmethod
    def update_user(
        user_id,
        username,
        password,
        role,
        image
    ):
        user = User.objects.filter(id=user_id).first()
        
        if not user:
            raise ValueError('User does not exist')
        
        user.username = username
        user.password = password
        user.role = role
        user.image = image
        
        user.save()
        
        return user

    @staticmethod
    def delete_user(
        user_id
    ):
        
        user = User.objects.filter(id=user_id).first()
        
        # Verify if user exist.
        if not user:
            raise ValueError('User does not exist')
        
        # Mark the user as inactive (logical delete) to preserve data integrity.
        if user.is_active:
            user.is_active = False
            
            user.save()
            
            return user
    
    @staticmethod
    def recover_user(
        user_id
    ):
        user = User.objects.filter(id=user_id).first()
        
        # Verify if user exist.
        if not user:
            raise ValueError('User does not exist')
        
        # Reactivate the user record by setting the status to active.
        if user.is_active == False:
            user.is_active = True
            
            user.save()
            
            return user