# Generated by Django 2.2 on 2020-05-17 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='m_info',
            name='score',
            field=models.CharField(default='6.0', max_length=5, verbose_name='评分'),
        ),
    ]
