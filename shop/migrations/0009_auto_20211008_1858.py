# Generated by Django 3.2.7 on 2021-10-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_signup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
