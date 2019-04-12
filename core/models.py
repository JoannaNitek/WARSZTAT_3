from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    capacity = models.IntegerField()
    has_projector = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    # def __str__(self):
    #     self.nazwa = 'Dodano nową salę o nazwie {}'.format(self.name)
    #     return self.nazwa
    # w ten sposób napis ten wyświetla się również przy modyfikacji lub usunięciu, więc lepiej
    # wrzucić tu jakąś uniwersalną wartość