from django.db import models
from django.utils import timezone 

# Create your models here.
class chaiVarity (models.Model):
    CHAI_TYPE_CHOICES = [
        ('black', 'Black Tea'),
        ('green', 'Green Tea'),
        ('herbal', 'Herbal Tea'),
        ('oolong', 'Oolong Tea'),
        ('white', 'White Tea'),
        ('chamomile', 'Chamomile Tea'),
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_added=models.DateTimeField(default =timezone.now)
    type=models.CharField(max_length=20, choices=CHAI_TYPE_CHOICES) 

    def __str__(self):
        return self.name
