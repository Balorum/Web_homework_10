# Generated by Django 4.2.1 on 2023-06-11 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0008_remove_quote_authors_quote_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]