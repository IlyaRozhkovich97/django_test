from django.urls import path

from main.apps import MainConfig
from main.views import contact, view_student, StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('student/<int:student_id>/', view_student, name='view_student'),
    path('create/', StudentCreateView.as_view(), name='create_student'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update_student'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),

]
