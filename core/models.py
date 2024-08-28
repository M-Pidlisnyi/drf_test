from django.db import models
from django_extensions.db.models import (
    TimeStampedModel, 
    ActivatorModel,
    TitleDescriptionModel
)
import uuid
# Create your models here.

class Contact(
    TimeStampedModel,
    ActivatorModel, 
    TitleDescriptionModel,
    models.Model
    ):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField()


    def __str__(self) -> str:
        return self.title
    
