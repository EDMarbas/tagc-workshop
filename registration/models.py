# registration/models.py
from django.db import models
from django.utils import timezone

AGE_CHOICES = [
        ('18-24', '18–24'),
        ('25-34', '25–34'),
        ('35-44', '35–44'),
        ('45+', '45 and above'),
    ]

EXPERIENCE_CHOICES = [
        ('Yes, as an independent freelancer (with direct clients)', 'Yes, as an independent freelancer (with direct clients)'),
        ('Yes, as part of a freelancing agency', 'Yes, as part of a freelancing agency'),
        ('Not yet, but I’ve created accounts and applied', 'Not yet, but I’ve created accounts and applied'),
        ('I’ve explored freelancing but haven’t applied', 'I’ve explored freelancing but haven’t applied'),
        ('No experience at all – I’m totally new to this!', 'No experience at all – I’m totally new to this!'),
    ]

EDUCATION_CHOICES = [
    ('Senior High School Student', 'Senior High School Student'),
    ('College Student', 'College Student'),
    ('College Graduate', 'College Graduate'),
    ('Master’s Student / Graduate', 'Master’s Student / Graduate'),
]

WORK_STATUS_CHOICES = [
    ('Employed', 'Employed'),
    ('Self-employed / Business Owner', 'Self-employed / Business Owner'),
    ('Unemployed', 'Unemployed'),
    ('Freelancer', 'Freelancer'),
    ('Part-time Worker', 'Part-time Worker'),
]

class Registration(models.Model):

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=100, help_text="City/Municipality")
    age_group = models.CharField(max_length=5, choices=AGE_CHOICES, blank=False)
    education = models.CharField(max_length=100, choices=EDUCATION_CHOICES, blank=False)
    course = models.CharField(max_length=100)
    work_status = models.CharField(max_length=100, choices=WORK_STATUS_CHOICES, blank=False)
    freelance_experience = models.CharField(max_length=100, choices=EXPERIENCE_CHOICES, blank=False)
    registered_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} ({self.email})"