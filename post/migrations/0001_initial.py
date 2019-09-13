# Generated by Django 2.2.5 on 2019-09-12 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('preview', models.TextField(max_length=500)),
                ('content', models.TextField(max_length=1000)),
                ('posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
