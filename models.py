from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)

    # campos de trazabilidad

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #visualización

    def __repr__(self) -> str:
        return f'{self.id} {self.title}'


class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    books = models.ManyToManyField(Books, related_name="authors")
    notes = models.CharField(max_length=255, default=False)

    # campos de trazabilidad

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #visualización

    def __repr__(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name}'
