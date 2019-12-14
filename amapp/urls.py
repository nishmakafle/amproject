from django.urls import *
from .views import *

app_name = "amapp"
urlpatterns = [
    # auth urls
    path('', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    # admin urls
    path('admin/', AdminHomeView.as_view(), name="adminhome"),
    path('admin/register/teacher/', AdminTeacherRegistrationView.as_view(),
         name="adminteacherregistration"),
    path('admin/list/teacher/', AdminTeacherListView.as_view(),
         name="adminteacherlist"),
    path('admin/detail/teacher-<int:pk>/',
         AdminTeacherDetailView.as_view(), name="adminteacherdetail"),
    path('admin/<int:pk>/teacher-update/',
         AdminTeacherUpdateView.as_view(), name='adminteacherupdate'),
    path('admin/<int:pk>/teacher-delete/',
         AdminTeacherDeleteView.as_view(), name='adminteacherdelete'),


    path('admin/student/create/', AdminStudentRegistrationView.as_view(),
         name='adminstudentregistration'),
    path('admin/student/list/', AdminStudentListView.as_view(),
         name='adminstudentlist'),
    path('admin/student/<int:pk>/update/',
         AdminStudentUpdateView.as_view(), name='adminstudentupdate'),
    path('admin/student/<int:pk>/delete/',
         AdminStudentDeleteView.as_view(), name='adminstudentdelete'),


    path('admin/program/create/', AdminProgramCreateView.as_view(),
         name='adminprogarmcreate'),
    path('admin/program/list/', AdminProgramListView.as_view(),
         name='adminprogramlist'),


    path('admin/classroom/create/', AdminClassRoomCreateView.as_view(),
         name='adminclassroomcreate'),
    path('admin/classroom/list/', AdminClassRoomListView.as_view(),
         name='adminclassroomlist'),
    # teacher urls

    path('teacher/home/', TeacherHomeView.as_view(), name='teacherhome'),
    path('teacher/assignment/create/',
         TeacherAssignmentCreateView.as_view(),
         name='teacherassignmnetcreate'),
    path('teacher/assignment-list/', TeacherAssignmentListView.as_view(),
         name='teacherassignmnetlist'),
    path('teacher/<int:pk>/assignment-update/',
         TeacherAssignmentUpdate.as_view(), name='teacherassignmnetupdate'),
    path('teacher/<int:pk>/assignment-delete/',
         TeacherAssignmentDeleteView.as_view(),
         name='teacherassignmentdelete'),
    path('teacher/detail-assignment-<int:pk>/',
         TeacherAssignmentDetailView.as_view(), name="teacherassignmentdetail"),
    path('teacher/submission-<int:pk>/review/',
         TeacherReviewView.as_view(), name="teacherreview"),

    # student urls


    path('student/home/', StudentHomeView.as_view(), name='studenthome'),
    path('student/list/assignment/', StudentAssignmentListView.as_view(),
         name="studentassignmentlist"),
    path('student/start-assignment-<int:pk>/',
         StudentAssignmentStartView.as_view(), name="studentassignmentstart"),
    path('student/detail/submission-<int:pk>/',
         StudentSubmissionDetailView.as_view(), name="studentsubmissiondetail"),
    path('student/upload-file-<sub_id>/', StudentFileUploadView.as_view(),
         name="studentfileupload"),

]
