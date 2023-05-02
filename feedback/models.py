from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django import forms

class Topic(models.Model):
    name = models.CharField(max_length=160)
    def __str__(self):
        return self.name

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="Aihe")
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name="Arvosana (0-5)")
    good = models.TextField(max_length=2000, blank=True, verbose_name="Hyvää")
    bad = models.TextField(max_length=2000, blank=True, verbose_name="Huonoa")
    ideas = models.TextField(max_length=2000, blank=True, verbose_name="Kehitysehdotukset")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'topic',)

    def __str__(self):
        return f"{self.date}"
