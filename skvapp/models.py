from django.db import models
from django.urls import reverse
from mainserver.Base import BaseModel
# Create your models here.
import uuid
from django_ckeditor_5.fields import CKEditor5Field

from django.contrib.auth.models import User

# function for forloop banner slider
def banner_slider_title():
    return f"skv-banner-{str(uuid.uuid4().hex[:8]).replace('-', '')}"


class BannerSlider(BaseModel):
    image = models.ImageField(upload_to='banner_slider/')
    title = models.CharField(
        max_length=255,
        default=banner_slider_title,
        help_text="This is a unique title for the banner slider",
    )
    description = models.TextField(default=f'This is a SKV banner slider')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Banner Slider'
        verbose_name_plural = 'Banner Sliders'
        ordering = ['order']
        db_table = 'banner_slider'
        unique_together = ('title', 'description')

    def __str__(self):
        return self.title
    
    
    def get_image_url(self):
        return self.image.url
    

class SKVEventDetail(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255)
    description = CKEditor5Field(config_name='extends')
    image = models.ImageField(upload_to='skv_event_detail/')
    event_initial_date = models.DateTimeField()
    event_final_date = models.DateTimeField()
    event_location = models.CharField(max_length=255)
    event_location_link = models.URLField(max_length=255, null=True, blank=True)
    event_organizer = models.CharField(max_length=255)
    event_contact = models.CharField(max_length=255)
    event_email = models.EmailField()

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'SKV Event Detail'
        verbose_name_plural = 'SKV Event Details'
        ordering = ['-created_at']
        db_table = 'skv_event_detail'
        unique_together = ('title', 'slug')

    def __str__(self):
        return self.title
    
    def get_image_url(self):
        return self.image.url
    
    def get_absolute_url(self):
        return reverse('skv_event_detail', kwargs={'slug': self.slug})

class SKVNewsDetail(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skv_news_detail_author', null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255)
    body = CKEditor5Field(config_name='extends')
    image = models.ImageField(upload_to='skv_news_detail/')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'SKV News Detail'
        verbose_name_plural = 'SKV News Details'
        ordering = ['-created_at']
        db_table = 'skv_news_detail'
        unique_together = ('title', 'slug')

    def __str__(self):
        return self.title
    
    def get_image_url(self):
        return self.image.url
    
    def get_absolute_url(self):
        return reverse('skv_news_detail', kwargs={'slug': self.slug})


class SKVHistory(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField(default=f'This is a SKV history')
    year = models.IntegerField(default=0, help_text='Enter the year of the history')
    image = models.ImageField(upload_to='skv_history/')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'SKV History'
        verbose_name_plural = 'SKV Histories'
        ordering = ['-order']
        db_table = 'skv_history'
        unique_together = ('title', 'year')
    
    def get_image_url(self):
        return self.image.url

    def __str__(self):
        return self.title
    