from rest_framework.urls import path


from establishment.views import (
    ListAddressView,
    AddressByIdView,
    AddressByStreetView,
    AddressByCityView,
    CreateAddressView,
    UpdateAddressView,
    ListInstitutionCategoryView,
    InstitutionCategoryByIdView,
    InstitutionCategoryByNameView,
    ListInstitutionView,
    InstitutionByIdView,
    InstitutionByCategoryView,
    InstitutionByNameView,
    InstitutionByCityView,
    CreateInstitutionView,
    UpdateInstitutionView,
    ListHistoryInstitutionView,
    HistoryInstitutionByIdView,
    HistoryInstitutionByInstitutionView,
    CreateHistoryInstitutionView,
    UpdateHistoryInstitutionView
)

urlpatterns = [
    # Views address
    path(
        'address/list/',
        ListAddressView.as_view(),
        name='list-address'
    ),
    path(
        'address/id/<int:id>',
        AddressByIdView.as_view(),
        name='address-by-id'
    ),
    path(
        'address/street/<str:street>',
        AddressByStreetView.as_view(),
        name='address-by-street'
    ),
    path(
        'address/city/id/<int:id>',
        AddressByCityView.as_view(),
        name='address-by-city'
    ),
    path(
        'address/create/',
        CreateAddressView.as_view(),
        name='create-address'
    ),
    path(
        'address/update/id/<int:id>',
        UpdateAddressView.as_view(),
        name='update-address'
    ),
    
    # Views category
    path(
        'category/list/',
        ListInstitutionCategoryView.as_view(),
        name='institution-category-list'
    ),
    path(
        'category/id/<int:id>',
        InstitutionCategoryByIdView.as_view(),
        name='institution-category-by-id'
    ),
    path(
        'category/institution/name/<str:name>',
        InstitutionCategoryByNameView.as_view(),
        name='institution-category-by-name'
    ),
    
    # Views institution
    path(
        'list/',
        ListInstitutionView.as_view(),
        name='list-institution'
    ),
    path(
        'id/<int:id>',
        InstitutionByIdView.as_view(),
        name='institution-by-id'
    ),
    path(
        'name/<str:name>',
        InstitutionByNameView.as_view(),
        name='institution-by-name'
    ),
    path(
       'category/name/<str:name>',
       InstitutionByCategoryView.as_view(),
       name='institution-by-category'
    ),
    path(
        'city/name/<str:name>',
        InstitutionByCityView.as_view(),
        name='institution-by-name'
    ),
    path(
        'create/',
        CreateInstitutionView.as_view(),
        name='create-institution'
    ),
    path(
        'update/id/<int:id>',
        UpdateInstitutionView.as_view(),
        name='update-institution'
    ),
    
    # Views history institution
    path(
        'history/list/',
        ListHistoryInstitutionView.as_view(),
        name='history-institution-list'
    ),
    path(
        'history/id/<int:id>',
        HistoryInstitutionByIdView.as_view(),
        name='history-institution-by-id'
    ),
    path(
        'history/institution/id/<int:id>',
        HistoryInstitutionByInstitutionView.as_view(),
        name='history-institution-by-institution'
        
    ),
    path(
        'history/create/',
        CreateHistoryInstitutionView.as_view(),
        name='create-history-institution'
    ),
    path(
        'history/update/id/<int:id>',
        UpdateHistoryInstitutionView.as_view(),
        name='update-history-institution'
    )
]
