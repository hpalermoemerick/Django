# Generated by Django 4.2.3 on 2023-10-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('no_reload', '0004_mensagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagem',
            name='remetente',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
