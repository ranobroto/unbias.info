# Generated by Django 2.1.2 on 2019-02-24 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190223_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleupload',
            name='biascolor',
            field=models.TextField(default='white'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articleupload',
            name='biastext',
            field=models.TextField(default='Not rated'),
            preserve_default=False,
        ),
    ]