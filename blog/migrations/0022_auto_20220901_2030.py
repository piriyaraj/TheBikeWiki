# Generated by Django 3.2.8 on 2022-09-01 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_blog_isupdated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikeimage',
            name='alt',
            field=models.TextField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='biketable',
            name='idofblog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_blogs', to='blog.blog'),
        ),
    ]