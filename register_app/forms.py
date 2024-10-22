from Glenda_App.models import Menu
from django.contrib.auth.forms import UserCreationForm
from django import forms

from register_app.models import department, designation, MenuPermissions


class department_Form(forms.ModelForm):
    class Meta:
        model = department
        fields = ['dept_Name']
        widgets = {
            'dept_Name': forms.Select(attrs={'class': 'form-control'}),

        }


class designation_Form(forms.ModelForm):
    class Meta:
        model = designation
        fields = ['user_type', 'dept']
        widgets = {
            'user_type': forms.Select(attrs={'class': 'form-control'}),
            'dept': forms.Select(attrs={'class': 'form-control'}),
        }




from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'phone_number',
            'designation',
            'department',
            'joining_date',
            'name',
            'password1',
            'password2',
        ]
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'designation': forms.Select(attrs={
                'class': 'form-control'
            }),  # This field will be dynamically populated via AJAX
            'department': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id_department'  # Important for the AJAX script to work
            }),
            'joining_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name'
            }),
        }

    # Override the password fields separately, ensuring they use PasswordInput widgets
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
    )


class CustomLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }),
        error_messages={
            'required': 'Please enter your email address.',
            'invalid': 'Enter a valid email address.'
        }
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }),
        error_messages={
            'required': 'Please enter your password.'
        }
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        # You can add any additional validation here if needed
        # For example, checking if email is in a specific domain

        return cleaned_data



class Permission_Form(forms.ModelForm):
    menu_details = forms.ModelMultipleChoiceField(
        queryset=Menu.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = MenuPermissions
        fields = ['menu_details',]