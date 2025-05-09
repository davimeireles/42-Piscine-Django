# Generated by Django 5.1.4 on 2025-04-29 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex10', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
