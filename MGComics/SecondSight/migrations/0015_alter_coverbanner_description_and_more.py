# Generated by Django 4.0.3 on 2022-05-09 19:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecondSight', '0014_alter_newspost_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverbanner',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='coverbanner',
            name='tag_line',
            field=ckeditor.fields.RichTextField(),
        ),
    ]