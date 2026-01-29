from rest_framework.urls import path


from academic.views import (
    ListSubjectView,
    SubjectByCourseView,
    SubjectByNameView,
    CreateSubjectView,
    UpdateSubjectView,
    DeleteSubjectView,
    RecoverSubjectView,
    CreateModalityAssistanceView,
    ListAssistanceView,
    AssistanceByStudentView,
    AssistanceByDateView,
    CreateAssistanceView,
    UpdateAssistanceView,
    ListDisciplinaryActionView,
    DisciplinaryActionByStudentView,
    DisciplinaryActionByDateView,
    CreateDisciplinaryActionView,
    UpdateDisciplinaryActionView,
    ListCourseView,
    CourseByNameView,
    CourseByInstitutionView,
    CreateCourseView,
    UpdateCourseView
)

urlpatterns = [
   # Subject urls
    path(
        'subject/list/',
        ListSubjectView.as_view(),
        name='list-subject'
    ),
    path(
        'subject/name/<str:name>',
        SubjectByNameView.as_view(),
        name='subject-by-name'
    ),
    path(
        'subject/course/<str:name>',
        SubjectByCourseView.as_view(),
        name='subject-by-course-name'
    ),
    path(
        'subject/create/',
        CreateSubjectView.as_view(),
        name='create-subject'
    ),
    path(
        'subject/update/<int:id>',
        UpdateSubjectView.as_view(),
        name='update-subject'
    ),
    path(
        'subject/delete/<int:id>',
        DeleteSubjectView.as_view(),
        name='delete-subject'
    ),
    path(
        'subject/status/<int:id>',
        RecoverSubjectView.as_view(),
        name='recover-subject'
    ),
    
    # Modality assistance urls
    path(
        'assistance/modality/create/',
        CreateModalityAssistanceView.as_view(),
        name='create-modality-assistance'
    ),
    
    # Assistance urls
    path(
        'assistance/list/',
        ListAssistanceView.as_view(),
        name='list-assistance'
    ),
    path(
        'assistance/date/<date>',
        AssistanceByDateView.as_view(),
        name='assistance-by-date'
    ),
    path(
        'assistance/student/<int:id>',
        AssistanceByStudentView.as_view(),
        name='assistance-by-student'
    ),
    path(
        'assistance/create/',
        CreateAssistanceView.as_view(),
        name='create-assistance'
    ),
    path(
        'assistance/update/<int:id>',
        UpdateAssistanceView.as_view(),
        name='update-assistance'
    ),
    
    # Disciplinary action urls
    path(
        'disciplinary/action/list/',
        ListDisciplinaryActionView.as_view(),
        name='list-disciplinary-action'
    ),
    path(
        'disciplinary/action/student/<str:name>',
        DisciplinaryActionByStudentView.as_view(),
        name='disciplinary-action-by-name'
    ),
    path(
        'disciplinary/action/date/<date>',
        DisciplinaryActionByDateView.as_view(),
        name='disciplinary-action-by-date'
    ),
    path(
        'disciplinary/action/create/',
        CreateDisciplinaryActionView.as_view(),
        name='action-disciplinary-action'
    ),
    path(
        'disciplinary/action/update/<int:id>',
        UpdateDisciplinaryActionView.as_view(),
        name='update-disciplinary-action'
    ),
    
    # Course urls
    path(
        'course/list/',
        ListCourseView.as_view(),
        name='list-course'
    ),
    path(
        'course/name/<str:name>',
        CourseByNameView.as_view(),
        name='course-by-name'
    ),
    path(
        'course/institution/name/<str:name>',
        CourseByInstitutionView.as_view(),
        name='course-by-institution'
    ),
    path(
        'course/create/',
        CreateCourseView.as_view(),
        name='create-course'
    ),
    path(
        'course/update/<int:id>',
        UpdateCourseView.as_view(),
        name='update-course'
    ),
]
