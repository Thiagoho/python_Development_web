from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Task

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.name
@receiver(post_save, sender=Task)   
def task_due_sonn(sender, instance, **kwargs):
    if instance.due_date - timezone.now().date() <= timezone.timedelta(days=2):
        # Logica para exibir notificaão 
        print(f'Tarefa "{instance.title}" está próxima do vencimento!')