# Generated by Django 5.1.1 on 2024-09-12 19:18

import catalog.languages
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_booklanguage_book_remove_booklanguage_languge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklanguage',
            name='name',
            field=models.CharField(choices=catalog.languages.book_languages, default='arabic', help_text='Book Language', max_length=2, unique=True),
        ),
    ]
