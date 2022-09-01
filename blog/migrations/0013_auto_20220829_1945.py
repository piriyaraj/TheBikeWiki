# Generated by Django 3.2.8 on 2022-08-29 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20220829_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikeimage',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_blogs', to='blog.blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_blogs', to='blog.biketable'),
        ),
    ]