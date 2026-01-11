from rest_framework.urls import path


from academic.views import (
    ListSubjectView,
    SubjectByIdView,
    SubjectByNameView,
    CreateSubjectView,
    UpdateSubjectView
)

urlpatterns = [
    path(
        'list/',
        ListSubjectView.as_view(),
        name='list-subject'
    ),
    path(
        'id/<int:id>',
        SubjectByIdView.as_view(),
        name='subject-by-id'
    ),
    path(
        'name/<str:name>',
        SubjectByNameView.as_view(),
        name='subject-by-name'
    ),
    path(
        'create/',
        CreateSubjectView.as_view(),
        name='create-subject'
    ),
    path(
        'update/<int:id>',
        UpdateSubjectView.as_view(),
        name='update-subject'
    ),
]
