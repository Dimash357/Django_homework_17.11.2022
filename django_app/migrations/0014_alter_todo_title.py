# Generated by Django 4.1.3 on 2022-11-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0013_delete_postcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(blank=True, db_index=True, default='', max_length=150, null=True, verbose_name='Заголовок'),
        ),
    ]
