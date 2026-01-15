from rest_framework.urls import path


from finance.views import (
    ListTeacherSalaryView,
    TeacherSalaryByIdView,
    TeacherSalaryByDateView,
    TeacherSalaryByTeacherView,
    CreateTeacherSalaryView,
    UpdateTeacherSalaryView
)

urlpatterns = [
    path(
        'list/',
        ListTeacherSalaryView.as_view(),
        name='list-teacher-salary'
    ),
    path(
        'id/<int:id>',
        TeacherSalaryByIdView.as_view(),
        name='teacher-salary-by-id'
    ),
    path(
        'date/<date>',
        TeacherSalaryByDateView.as_view(),
        name='teacher-salary-by-date'
    ),
    path(
        'teacher/<int:id>',
        TeacherSalaryByTeacherView.as_view(),
        name='teacher-salary-by-teacher-id'
    ),
    path(
        'create/',
        CreateTeacherSalaryView.as_view(),
        name='create-teacher-salary'
    ),
    path(
        'update/id/<int:id>',
        UpdateTeacherSalaryView.as_view(),
        name='update-teacher-salary'
    ),
]
