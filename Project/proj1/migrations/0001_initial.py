# Generated by Django 2.2.4 on 2019-08-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home_Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('bodytext', models.TextField(blank=True, verbose_name='Page Content')),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
