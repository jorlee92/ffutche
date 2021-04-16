from django.urls import path
from home.api import views
app_name =  'home'


urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/<pk>/', views.UserDetailView.as_view(), name='subject_detail'),
    path('schools/', views.SchoolListView.as_view(), name='school_list'),
    path('schools/<pk>/', views.SchoolDetailView.as_view(), name='school_detail'),
    path('scholarips/', views.ScholarshipListView.as_view(), name='scholarship_list'),
    path('scholarips/<pk>/', views.ScholarshipDetailView.as_view(), name='scholarship_detail'),   
    path('tuition_fees/', views.TuitionFeesListView.as_view(), name='tuition_fees_list'),
    path('tuition_fees/<pk>/', views.TuitionFeesDetailView.as_view(), name='school_detail'),   
]