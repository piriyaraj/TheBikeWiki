# Generated by Django 3.2.8 on 2022-08-29 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_bikeimage_biketable'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='table',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='blog.biketable'),
        ),
    ]
