from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from djmoney.models.fields import MoneyField


class Worships(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=1000, blank=False)
    start_time = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    price = models.FloatField(default=0)
    slug = models.SlugField(null=False, unique=True)
    images = models.ImageField(upload_to='static/worship_images/', default="profile_default.jpeg", blank=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("worship_details", kwargs={"slug": self.slug})
