from rest_framework.urls import path


from grades.views import (
	ListAssessmentCategoryView,
 	CreateAssessmentCategoryView,
	ListGradesView,
	GradesBySubjectView,
	GradesByTermView,
	GradesByStudentView,
	CreateGradesView,
 	UpdateGradesView
)

urlpatterns = [
	# Assessment category urls
 	path(
		'assessment/category/list/',
		ListAssessmentCategoryView.as_view(),
		name='list-assessment-category'
    ),
	path(
		'assessment/category/create/',
  		CreateAssessmentCategoryView.as_view(),
    	name='create-assessment-category'
    ),
	
	# Grandes urls
	path(
		'list/',
		ListGradesView.as_view(),
		name='list-grades'
    ),
	path(
		'subject/name/<str:name>',
		GradesBySubjectView.as_view(),
		name='grades-by-name'
    ),
	path(
		'term/<str:term>',
		GradesByTermView.as_view(),
		name='grades-by-term'
    ),
	path(
		'student/<str:name>',
		GradesByStudentView.as_view(),
		name='grades-by-student'
	),
	path(
		'create/',
		CreateGradesView.as_view(),
		name='create-grades'
    ),
	path(
		'update/<int:id>',
		UpdateGradesView.as_view(),
		name='update-grades'
    ),
]
