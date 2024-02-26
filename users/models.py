from django.db import models
from abstractModels.abstractModel import BaseModel
from django.contrib.auth.hashers import make_password


class User(BaseModel):
    username = models.CharField(max_length=256, null=True, blank=True)
    mainimg = models.ImageField(upload_to='users/', null=True, blank=True)
    password = models.CharField(max_length=256, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_main_image_url(self):
        return self.mainimg.url if self.mainimg else None