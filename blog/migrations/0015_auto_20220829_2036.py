# Generated by Django 3.2.8 on 2022-08-29 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20220829_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='category',
            new_name='blogcategory',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='user',
            new_name='bloguser',
        ),
    ]
