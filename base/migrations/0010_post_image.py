# Generated by Django 4.2.3 on 2023-10-07 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_post_body3'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='base/images/AI.jpg'),
        ),
    ]