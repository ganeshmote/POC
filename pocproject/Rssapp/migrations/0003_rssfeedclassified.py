# Generated by Django 2.0 on 2020-01-14 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rssapp', '0002_auto_20200113_0705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rssfeedclassified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=300)),
                ('Link', models.CharField(max_length=300)),
                ('Publish_date', models.CharField(max_length=300)),
                ('Description', models.TextField()),
                ('classification', models.CharField(max_length=300)),
                ('insertDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
