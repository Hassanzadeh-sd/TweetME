from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.timesince import timesince
class Tweet(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    content     = models.TextField(max_length=140)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk": self.pk})
   
    class Meta:
        ordering = ['-timestamp','content']

    def __str__(self):
        return self.content

    def get_date_display(self):
        return self.timestamp.strftime("%b %d, %Y | at %I:%M %p")

    def get_timesince(self):
        return timesince(self.timestamp) + " ago"        