# registration/forms.py
from django import forms
from .models import Registration, AGE_CHOICES, EXPERIENCE_CHOICES, EDUCATION_CHOICES, WORK_STATUS_CHOICES

class RegistrationForm(forms.ModelForm):
    # --- Explicitly define the choice fields here ---
    age_group = forms.ChoiceField(
        label='Age Group', # Add asterisk for required visual cue
        choices=AGE_CHOICES, # Use the choices list from models.py
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=True # Make the form field explicitly required
    )
    freelance_experience = forms.ChoiceField(
        label='Do you have any experience in Online Freelancing?',
        choices=EXPERIENCE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=True
    )

    education = forms.ChoiceField(
        label='What is your current educational status?',
        choices=EDUCATION_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=True
    )

    work_status = forms.ChoiceField(
        label='Employment Status',
        choices=WORK_STATUS_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=True
    )    
    # --- End explicit definitions ---

    class Meta:
        model = Registration

        fields = [
            'full_name',
            'email',
            'location',
            'age_group',
            'freelance_experience',
            'education',
            'work_status',
            'course',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First and Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City/Municipality'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., STEM, BSBA in Marketing, AB English'}),
         
        }
        labels = {
            'full_name': 'Full Name (First and Last Name) *',
            'email': 'Email Address *',
            'location': 'Location (City/Municipality) *',
            'course': 'Course / Major:'
        }
