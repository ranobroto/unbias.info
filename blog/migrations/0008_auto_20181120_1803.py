# Generated by Django 2.1.2 on 2018-11-20 23:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_auto_20181120_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleupload',
            name='num_vote_down',
        ),
        migrations.RemoveField(
            model_name='articleupload',
            name='num_vote_up',
        ),
        migrations.RemoveField(
            model_name='articleupload',
            name='vote_score',
        ),
        migrations.RemoveField(
            model_name='articleupload',
            name='votes',
        ),
        migrations.AddField(
            model_name='articleupload',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
