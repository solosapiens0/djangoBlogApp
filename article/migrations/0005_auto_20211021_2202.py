# Generated by Django 3.2.8 on 2021-10-21 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-createdDate']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-commentDate']},
        ),
    ]
