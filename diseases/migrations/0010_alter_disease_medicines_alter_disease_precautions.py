# Generated by Django 5.0.4 on 2024-11-21 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0009_alter_disease_medicines_alter_disease_precautions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='medicines',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='disease',
            name='precautions',
            field=models.TextField(),
        ),
    ]
