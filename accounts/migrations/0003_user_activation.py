# Generated by Django 3.2.6 on 2021-08-08 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Activation'),
        ),
    ]
