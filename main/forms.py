from django import forms
from main.models import Student


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StudentForm(StyleFormMixin, forms.ModelForm):  # Исправлено
    class Meta:
        model = Student
        fields = ("first_name", "last_name", "avatar", 'email')
        # Если вы хотите использовать все поля, можно использовать:
        # fields = "__all__"
        # или исключить определенные поля:
        # exclude = ("is_active",)

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']

        if 'sky.pro' not in cleaned_data:
            raise forms.ValidationError('Почта должна относиться к учебному заведению')

        return cleaned_data
