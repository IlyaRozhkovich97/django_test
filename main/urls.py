from django.urls import path

from main.apps import MainConfig
from main.views import contact, view_student, StudentListView, StudentDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('student/<int:student_id>/', view_student, name='view_student'),  # Исправлено
]
