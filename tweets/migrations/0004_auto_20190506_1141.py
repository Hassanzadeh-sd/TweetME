# Generated by Django 2.2.1 on 2019-05-06 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_tweet_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-timestamp', 'content']},
        ),
    ]
