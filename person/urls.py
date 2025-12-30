from rest_framework.urls import path


from person.views import (
    ListGenreView,
    GenreByIdView,
    GenreByNameView,
    ListIdentityDocumentView,
    IdentityDocumentByIdView,
    IdetityDocumentByNameView,
    ListMaritalStatusView,
    MaritalStatusByIdView,
    MaritalStatusByNameView
)


urlpatterns = [
    path(
        'genre/list',
        ListGenreView.as_view(),
        name='genre-list'
    ),
    path(
        'genre/id/<int:id>',
        GenreByIdView.as_view(),
        name='genre-by-id'
    ),
    path(
        'genre/name/<str:name>',
        GenreByNameView.as_view(),
        name='genre-by-name'
    ),
    path(
        'identity/document/list',
        ListIdentityDocumentView.as_view(),
        name='identity-document-list'
    ),
    path(
        'identity/document/id/<int:id>',
        IdentityDocumentByIdView.as_view(),
        name='identity-document-by-id'
    ),
    path(
        'identity/document/name/<str:name>',
        IdetityDocumentByNameView.as_view(),
        name='identity-document-by-name'
    ),
    path(
        'marital/status/list',
        ListMaritalStatusView.as_view(),
        name='marital-status-list'
    ),
    path(
        'marital/status/id/<int:id>',
        MaritalStatusByIdView.as_view(),
        name='marital-status-by-id'
    ),
    path(
        'marital/status/name/<str:name>',
        MaritalStatusByNameView.as_view(),
        name='marital-status-name'
    ),
]