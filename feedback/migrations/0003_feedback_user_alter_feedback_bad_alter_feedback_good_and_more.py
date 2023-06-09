# Generated by Django 4.2 on 2023-05-02 10:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0002_feedback_ideas_alter_feedback_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='bad',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Huonoa'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='good',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Hyvää'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='ideas',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Kehitysehdotukset'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Arvosana (0-5)'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.topic', verbose_name='Aihe'),
        ),
        migrations.AlterUniqueTogether(
            name='feedback',
            unique_together={('user', 'topic')},
        ),
    ]
