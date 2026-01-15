from rest_framework.urls import path


from teacher_institution.views import(
    ListTeachingFileView,
    TeachingFileByIdView,
    TeachingFileByNumberView,
    CreateTeachingFileView,
    UpdateTeachingFileView,
    ListTeachingAssistanceView,
    TeachingAssistanceByIdView,
    TeachingAssistanceByNameView,
    TeachingAssistanceByDateView,
    CreateTeachingAssistanceView,
    UpdateTeachingAssistanceView,
    ListTeacherView,
    TeacherByIdView,
    TeacherByNameView,
    CreateTeacherView
)


urlpatterns = [
    # Teaching file path
    path(
        'file/list/',
        ListTeachingFileView.as_view(),
        name='list-teaching-file'
    ),
    path(
        'file/id/<int:id>',
        TeachingFileByIdView.as_view(),
        name='teaching-file-by-id'
    ),
    path(
        'file/number/<str:number>',
        TeachingFileByNumberView.as_view(),
        name='teaching-file-by-number'
    ),
    path(
        'file/create/',
        CreateTeachingFileView.as_view(),
        name='create-teaching-file'
    ),
    path(
        'file/update/id/<int:id>',
        UpdateTeachingFileView.as_view(),
        name='update-teaching-file'
    ),
    
    # Teaching assistance path
    path(
        'assistance/list/',
        ListTeachingAssistanceView.as_view(),
        name='list-teaching-assistance'
    ),
    path(
        'assistance/id/<int:id>',
        TeachingAssistanceByIdView.as_view(),
        name='teeaching-assistance-by-id'
    ),
    path(
        'name/assistance/<str:name>',
        TeachingAssistanceByNameView.as_view(),
        name='teaching-assistance-by-name'
    ),
    path(
        'assistance/date/<date>',
        TeachingAssistanceByDateView.as_view(),
        name='teaching-assistance-by-date'
    ),
    path(
        'assistance/create/',
        CreateTeachingAssistanceView.as_view(),
        name='create-teaching-assistance'
    ),
    path(
        'assistance/update/id/<int:id>',
        UpdateTeachingAssistanceView.as_view(),
        name='update-teaching-assistance'
    ),
    
    # Teacher path
    path(
        'list/',
        ListTeacherView.as_view(),
        name='list-teacher'
    ),
    path(
        'name/<str:name>',
        TeacherByNameView.as_view(),
        name='teacher-by-name'
    ),
    path(
        'id/<int:id>',
        TeacherByIdView.as_view(),
        name='teacher-by-id'
    ),
    path(
        'create/',
        CreateTeacherView.as_view(),
        name='create-teacher'
    ),
]
