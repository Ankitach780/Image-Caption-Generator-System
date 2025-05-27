from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CaptionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    image = models.ImageField(upload_to='images/')
    caption = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.caption[:30]}..."
