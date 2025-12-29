from rest_framework.permissions import IsAuthenticated, IsAdminUser

class AuthView:
    permission_classes = [IsAuthenticated]
    
class AuthAdminView:
    permission_classes = [IsAdminUser]