# Generated by Django 4.1.1 on 2023-02-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.CharField(default='사용가능', max_length=100),
        ),
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.BooleanField(default=True),
        ),
    ]
