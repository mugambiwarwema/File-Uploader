# Generated by Django 3.1.7 on 2021-03-02 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
