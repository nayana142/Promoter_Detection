# Create your models here.
from django.db import models

class DNASequence(models.Model):
    sequence = models.CharField(max_length=100)  # Assuming DNA sequences are less than 100 nucleotides
    affected_by_ecoli = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sequence
    