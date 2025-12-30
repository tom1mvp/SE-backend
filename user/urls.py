from django.urls import path

from user.views import (
    ListUserView,
    UserByIdView,
    UserByRoleView,
    UserByUsernameView,
    LoginView,
    RegisterView,
    UpdateUserView,
    DeleteUserView,
    RecoverUserView
)

urlpatterns = [
    path(
        'list/',
        ListUserView.as_view(),
        name='list-users'
    ),
    
    path(
        'id/<int:id>',
        UserByIdView.as_view(),
        name='user-by-id'
    ),
    
    path(
        'role/<str:role>',
        UserByRoleView.as_view(),
        name='user-by-role'
    ),
    
    path(
        'name/<str:username>',
        UserByUsernameView.as_view(),
        name='user-by-username'
    ),
    
    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),
    
    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),
    
    path(
        'update/<int:id>',
        UpdateUserView.as_view(),
        name='update-user'
    ),
    
    path(
        'delete/<int:id>',
        DeleteUserView.as_view(),
        name='delete-user'
    ),
    
    path(
        'status/<int:id>',
        RecoverUserView.as_view(),
        name='recover-user'
    )
]
