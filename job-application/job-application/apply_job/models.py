from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# This model is for admin to add new job to website
class Position(models.Model):
    title = models.CharField(max_length=30, blank=True)
    description = models.TextField(null=True, blank=True)

    # setting how to display positions in the django admin panel
    def __str__(self):
        return self.title


# main model for the application form
class JobApplication(models.Model):
    # Choices for a radio button for gender
    GENDER = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    # choices for selecting experience
    EXPERIENCE = [
        ("1", "Fresher"),
        ("2", "1-2 years"),
        ("3", "3-5 years"),
        ("4", "6-8 years"),
        ("5", "8+ years"),
    ]
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    # automatic validation for US phone numbers
    phone_number = PhoneNumberField(region="US", blank=True)
    date_of_birth = models.DateField(blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=50, blank=True)
    nationality = models.CharField(max_length=30, blank=True)
    # Position model as forign key, so that user can select the job
    # delete every job application when that job is expired
    position_applying = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True)
    # experience in years
    experience = models.CharField(max_length=20, choices=EXPERIENCE, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True)
    # automatically update the date and time applied when applying and editing
    date_applied = models.DateTimeField(auto_now=True, blank=True)
    expected_ctc = models.CharField(max_length=50, blank=True)
    current_ctc = models.CharField(max_length=50, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)

    # how to display the class in the django admin panel
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
