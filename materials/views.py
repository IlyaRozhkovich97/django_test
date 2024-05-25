from django.views.generic import CreateView, ListView
from materials.models import Material
from django.urls import reverse_lazy


class MaterialsCreateView(CreateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy("materials:list")


class MaterialListView(ListView):
    model = Material

