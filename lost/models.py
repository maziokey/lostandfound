from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the name or title of lost object')
    type_of_object = models.CharField(max_length=200, help_text='What type of object are you posting')
    description = models.TextField(max_length=1000)
    location_found = models.TextField(max_length=300, help_text='Where did you find the object?')
    pickup_details = models.TextField(max_length=300, help_text='Details of pickup location')
    posted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    AVAILABLE = 'AVAILABLE'
    PICKED_UP = 'PICKED UP'
    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (PICKED_UP, 'Picked Up'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=12, blank=True, default=AVAILABLE)
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
