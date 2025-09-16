from django.db import models
from mainserver.Base import BaseModel

# Create your models here.

class Newsletter(BaseModel):
    email = models.EmailField(unique=True, max_length=255, help_text='Enter your email address')
    is_active = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)

    def is_subscribed(self):
        return self.is_subscribed


    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
        ordering = ['-created_at']
        db_table = 'skv_newsletter'
        unique_together = ('email',)

    def __str__(self):
        return self.email
