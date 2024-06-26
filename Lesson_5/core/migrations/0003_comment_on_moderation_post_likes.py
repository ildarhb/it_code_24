# Generated by Django 5.0.4 on 2024-05-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='on_moderation',
            field=models.BooleanField(default=True, verbose_name='На модерации'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Лайки'),
        ),
    ]
