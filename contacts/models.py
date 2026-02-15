from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    CATEGORY_CHOICES = [
        ('Family', 'Family'),
        ('Friend', 'Friend'),
        ('Work', 'Work'),
        ('Emergency', 'Emergency'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
