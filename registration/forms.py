# registration/forms.py
from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            'full_name',
            'email',
            'location',
            'age_group',
            'current_situation',
            'freelance_experience',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First and Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City/Municipality'}),
            'age_group': forms.RadioSelect(attrs={'class': 'form-check-input'}), # Use RadioSelect for better UX
            'current_situation': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'freelance_experience': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'full_name': 'Full Name (First and Last Name) *',
            'email': 'Email Address *',
            'location': 'Location (City/Municipality) *',
            'age_group': 'Age Group',
            'current_situation': 'What best describes your current situation?',
            'freelance_experience': 'Do you have any experience in Online Freelancing?',
        }

    # Optional: Add custom cleaning/validation if needed
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     # Add custom email validation logic here if needed
    #     return email