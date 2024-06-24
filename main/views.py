from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Student
from main.forms import StudentForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'main/index.html'
    context_object_name = 'objects_list'
    extra_context = {'title': 'Главная'}


@login_required
@permission_required('mian.view_student')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Сообщение из формы обратной связи:\nФИО: {name}\nЭлектонная почта: {email}\nСообщение: {message}")

    context = {
        'title': 'Контакт'
    }

    return render(request, 'main/contact.html', context)


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'main/student_detail.html'
    context_object_name = 'student'
    extra_context = {'title': 'Студент'}


@login_required
@permission_required
def view_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {'student': student}
    return render(request, 'main/student_detail.html', context)


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    permission_required = 'main.add_student'
    success_url = reverse_lazy('main:index')


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    permission_required = 'main.chandge_student'
    success_url = reverse_lazy('main:index')


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Student
    permission_required = 'main.delete_student'
    success_url = reverse_lazy('main:index')
