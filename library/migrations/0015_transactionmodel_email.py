# Generated by Django 5.1 on 2024-09-14 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_remove_issuedbook_expirydate_transactionmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionmodel',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]