from rest_framework.urls import path


from academic.views import (
    ListSubjectView,
    SubjectByIdView,
    SubjectByNameView,
    CreateSubjectView,
    UpdateSubjectView,
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
    UpdateDisciplinaryActionView
)

urlpatterns = [
   # Subject urls
    path(
        'subject/list/',
        ListSubjectView.as_view(),
        name='list-subject'
    ),
    path(
        'subject/id/<int:id>',
        SubjectByIdView.as_view(),
        name='subject-by-id'
    ),
    path(
        'subject/name/<str:name>',
        SubjectByNameView.as_view(),
        name='subject-by-name'
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
]
