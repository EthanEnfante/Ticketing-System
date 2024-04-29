from django.db import models

# Create your models here.
class Ticket(models.Model):
    PRIORITY_CHOICES = {
        'L': 'Low',
        'M': 'Medium',
        'H': 'High',
        'U': 'Urgent'
    }
    CASE_SEVERITY_OPTIONS = {
        'S1': 'One to three users',
        'S2': 'Four to ten users',
        'S3': 'Eleven to 20 users'
    }
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    issue_type = models.CharField(max_length=30)
    issue_title = models.CharField(max_length=30)
    issue_description = models.CharField(max_length=255)
    date_submitted = models.DateTimeField()
    case_severity = models.IntegerField(max_length=2, choices=CASE_SEVERITY_OPTIONS, null=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, null=True)
    user_assigned = models.IntegerField(null=True)