from django import forms

from .models import Interview


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['name', 'description', 'end_date']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style':'width: 300px;'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'style':'width: 300px;', 'size': '40'}),
            'end_date': forms.SelectDateWidget(attrs={'class': 'form-control mb-3', 'style':'width: 300px;'})
        }
