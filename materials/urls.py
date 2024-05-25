from django.urls import path

from materials.apps import MaterialsConfig

from materials.views import MaterialsCreateView, MaterialListView


app_name = MaterialsConfig.name

urlpatterns = [
    path('create/', MaterialsCreateView.as_view(), name='create'),
    path('', MaterialListView.as_view(), name='list'),
    # path('view/<int:pk>/', ..., name='view'),
    # path('edit/<int:pk>/', ..., name='edit'),
    # path('delete/<int:pk>/', ..., name='delete'),
]
