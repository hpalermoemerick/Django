# Generated by Django 4.2.3 on 2023-10-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('no_reload', '0003_delete_mensagem_alter_profile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
