from django.db import models
from django.conf import settings

class Notice(models.Model):
    # Assuming the author is a User model instance
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notice by {self.author.username} on {self.created_at.strftime('%Y-%m-%d')}"

class CourseMaterial(models.Model):
    chapter_name = models.CharField(max_length=255)
    notes = models.FileField(upload_to='notes/')
    video_url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chapter_name
