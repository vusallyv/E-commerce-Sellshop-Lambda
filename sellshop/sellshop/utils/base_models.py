from django.db import models


# from django.utils import timezone
class BaseModel(models.Model):
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True