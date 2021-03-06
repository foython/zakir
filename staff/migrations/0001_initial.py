# Generated by Django 3.1.7 on 2022-01-13 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('position', models.CharField(choices=[('1', 'Senior Faculty Member'), ('2', 'Faculty Member')], max_length=32)),
                ('facebook_link', models.URLField(max_length=64)),
                ('twitter_link', models.URLField(max_length=64)),
                ('linkedin_link', models.URLField(max_length=64)),
                ('image', models.ImageField(upload_to='staff/')),
            ],
        ),
    ]
