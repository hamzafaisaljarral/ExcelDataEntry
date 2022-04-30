from django import forms
from .models import Employee


# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = ['empcode', 'firstname']
#
#
# class EmployeeBulkForm(EmployeeForm):
#     file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#
#     class Meta(EmployeeForm.Meta):
#         fields = EmployeeForm.Meta.fields + ['file', ]
