# Generated by Django 3.2 on 2022-05-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
    ]
