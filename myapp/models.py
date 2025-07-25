from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=False, blank=False) # jeigu lyginsim po to ateityje svarbu DateTimeField ne DateField # false padareme,kad butu ivedamass butinai laukas
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['completed', 'due_date']

    def __str__(self):
        return self.title

    def is_overdue(self):
        return self.due_date and self.due_date < timezone.now() and not self.completed