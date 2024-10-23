from django import forms
from .models import EmployeeDetails

class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = ['emergency_contact_number','aadhar_no','street','pincode','state','country','landmark','district']
