from django.db import models
class KnowledgeItem(models.Model):
    question = models.TextField()
    answer = models.TextField()
from django.db import models

class KnowledgeItem(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

    def __str__(self):
        return self.question[:50]

class Message(models.Model):
    MEDIA_CHOICES = (
        ('text', 'Text'),
        ('image', 'Image'),
        ('audio', 'Audio'),
    )
    sender = models.CharField(max_length=32)
    content = models.TextField(blank=True, null=True)
    media_type = models.CharField(max_length=5, choices=MEDIA_CHOICES)
    media_file = models.FileField(upload_to='uploads/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)