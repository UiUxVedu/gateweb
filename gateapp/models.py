from django.db import models

class StudentApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100)

    COURSE_CHOICES = [
        ('GATE-CS', 'GATE Computer Science'),
        ('GATE-EC', 'GATE Electronics'),
        ('GATE-EE', 'GATE Electrical'),
        ('GATE-ME', 'GATE Mechanical'),
    ]
    course = models.CharField(max_length=20, choices=COURSE_CHOICES)

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.course})"
