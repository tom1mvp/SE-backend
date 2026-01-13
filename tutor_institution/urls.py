from rest_framework.urls import path


from tutor_institution.views import (
    ListTutorView,
    TutorByIdView,
    TutorByNameView,
    TutorByRelationship,
    CreateTutorView
)

urlpatterns = [
    path(
        'list/',
        ListTutorView.as_view(),
        name='list-tutor'
    ),
    path(
        'id/<int:id>',
        TutorByIdView.as_view(),
        name='tutor-by-id'
    ),
    path(
        'name/<str:name>',
        TutorByNameView.as_view(),
        name='tutor-by-name'
    ),
    path(
        'relationship/<str:relationship>',
        TutorByRelationship.as_view(),
        name='tutor-by-relationship'
    ),
    path(
        'create/',
        CreateTutorView.as_view(),
        name='create-tutor'
    ),
]
