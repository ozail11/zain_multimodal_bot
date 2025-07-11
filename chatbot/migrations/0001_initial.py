# Generated by Django 5.2.3 on 2025-06-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=32)),
                ('content', models.TextField(blank=True, null=True)),
                ('media_type', models.CharField(choices=[('text', 'Text'), ('image', 'Image'), ('audio', 'Audio')], max_length=5)),
                ('media_file', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
