# Generated by Django 4.0.4 on 2022-07-13 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.CharField(default='https://images-na.ssl-images-amazon.com/images/I/81l3rZK4lnL.jpg', max_length=500),
        ),
    ]
