from django.db import models

class Application(models.Model):

    COURSE_CHOICES = [
        ('CS', 'Computer Science'),
        ('ENTC', 'Electronics & Telecommunication'),
        ('EE', 'Electrical Engineering'),
        ('ME', 'Mechanical Engineering'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
