from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)

    def __str__(self):
        return self.title

class Quote(models.Model):
        text = models.TextField()
        chapter_verse = models.CharField(max_length=100)
        language = models.CharField(max_length=50, default='English')
        is_active = models.BooleanField(default=True)
   
def __str__(self):
    return self.text[:50]+" - " +self.chapter_verse#the quote text

