# registration/models.py
from django.db import models
from django.utils import timezone

class Registration(models.Model):
    AGE_CHOICES = [
        ('18-24', '18–24'),
        ('25-34', '25–34'),
        ('35-44', '35–44'),
        ('45+', '45 and above'),
    ]

    SITUATION_CHOICES = [
        ('shs', 'Senior High School Student/Graduate'),
        ('college', 'College Student'),
        ('unemployed', 'Unemployed'),
        ('employed', 'Employed'),
        ('self_employed', 'Self-employed/business owner'),
    ]

    EXPERIENCE_CHOICES = [
        ('independent', 'Yes, as an independent freelancer (with direct clients)'),
        ('agency', 'Yes, as part of a freelancing agency'),
        ('applied', 'Not yet, but I’ve created accounts and applied'),
        ('explored', 'I’ve explored freelancing but haven’t applied'),
        ('none', 'No experience at all – I’m totally new to this!'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) # unique=True prevents duplicate emails
    location = models.CharField(max_length=100, help_text="City/Municipality")
    age_group = models.CharField(max_length=5, choices=AGE_CHOICES)
    current_situation = models.CharField(max_length=20, choices=SITUATION_CHOICES)
    freelance_experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    registered_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} ({self.email})"