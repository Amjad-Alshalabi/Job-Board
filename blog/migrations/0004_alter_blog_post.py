# Generated by Django 3.2.8 on 2021-11-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post',
            field=models.TextField(max_length=10000),
        ),
    ]
