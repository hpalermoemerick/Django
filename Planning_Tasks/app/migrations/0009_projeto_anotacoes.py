# Generated by Django 4.2.7 on 2023-11-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_mensagemforum'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='anotacoes',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]
