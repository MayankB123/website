# Generated by Django 4.2.3 on 2023-07-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_post_body1_post_body2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
