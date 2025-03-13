# Generated by Django 5.1.6 on 2025-02-28 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clicklate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translated',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text_boolean', models.BooleanField()),
                ('image_boolean', models.BooleanField()),
                ('date_translated', models.DateField()),
                ('detected_language', models.CharField(max_length=40)),
                ('translate_to_language', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='clicklate',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
