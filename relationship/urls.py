from rest_framework.urls import path


from relationship.views import (
	ListRelationshipView,
	RelationshipByKinshipView,
	RelatioshipByTutorView,
	CreateRelationshipView,
	UpdateRelationshipView,
	DeleteRelationshipView,
	RecoverRelationshipView
)

urlpatterns = [
	path(
		'list/',
		ListRelationshipView.as_view(),
		name='list-relationship'
    ),
	path(
		'kinship/<str:kinship>',
		RelationshipByKinshipView.as_view(),
		name='relationship-by-kinship'
    ),
 	path(
		'tutor/<str:name>',
		RelatioshipByTutorView.as_view(),
		name='relationship-by-tutor'
    ),
	path(
		'create/',
		CreateRelationshipView.as_view(),
		name='create-relationship'
    ),
	path(
		'update/<int:id>',
		UpdateRelationshipView.as_view(),
		name='update-relationship'
    ),
	path(
		'delete/<int:id>',
		DeleteRelationshipView.as_view(),
		name='delete-relationship'
    ),
	path(
		'status/<int:id>',
		RecoverRelationshipView.as_view(),
		name='recover-relationship'
	)
]
