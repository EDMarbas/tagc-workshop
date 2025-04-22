# registration/forms.py
from django import forms
# Import the model AND the choices lists from your models file
from .models import Registration, AGE_CHOICES, SITUATION_CHOICES, EXPERIENCE_CHOICES

class RegistrationForm(forms.ModelForm):
    # --- Explicitly define the choice fields here ---
    age_group = forms.ChoiceField(
        label='Age Group', # Add asterisk for required visual cue
        choices=AGE_CHOICES, # Use the choices list from models.py
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=True # Make the form field explicitly required
    )
    current_situation = forms.ChoiceField(
        label='Which option best describes your current situation?',
        choices=SITUATION_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=True
    )
    freelance_experience = forms.ChoiceField(
        label='Do you have any experience in Online Freelancing?',
        choices=EXPERIENCE_CHOICES,
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
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First and Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City/Municipality'}),
         
        }
        labels = {
            'full_name': 'Full Name (First and Last Name) *',
            'email': 'Email Address *',
            'location': 'Location (City/Municipality) *',
        }
