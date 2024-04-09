# Generated by Django 5.0.4 on 2024-04-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marksheetmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Math', models.IntegerField()),
                ('Science', models.IntegerField()),
                ('Social_science', models.IntegerField()),
                ('Hindi', models.IntegerField()),
                ('English', models.IntegerField()),
                ('Total_marks', models.IntegerField()),
                ('Percentage', models.IntegerField()),
            ],
        ),
    ]