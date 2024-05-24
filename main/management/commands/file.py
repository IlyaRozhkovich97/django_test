from django.core.management import BaseCommand
from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {"last_name": "Рожкович", "first_name": "Илья"},
            {"last_name": "Рожкович", "first_name": "Артем"},
            {"last_name": "Рожкович", "first_name": "Мария"}
        ]

        # for student_items in student_list:
        # Student.objects.create(**student_items)

        students_for_create = []

        for student_items in student_list:
            students_for_create.append(Student(**student_items))

        Student.objects.bulk_create(students_for_create)
