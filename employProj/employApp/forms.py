from django import forms

# EMPLOYEE FORM
class EmployeeForm(forms.Form):
    name = forms.CharField()
    dob = forms.DateField()
    position = forms.CharField()
    salary = forms.IntegerField()