# Generated by Django 4.0.3 on 2022-04-27 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecondSight', '0002_alter_comic_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='image',
            field=models.ImageField(default=2, upload_to='images/'),
            preserve_default=False,
        ),
    ]