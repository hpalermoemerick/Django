# Generated by Django 4.2.7 on 2023-11-25 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_codigo_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='codigo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.codigo'),
        ),
    ]
