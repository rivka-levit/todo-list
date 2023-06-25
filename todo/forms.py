from django import forms
from .models import Task


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(EditTaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
