# Generated by Django 5.1 on 2024-09-14 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_alter_transactionmodel_returndate'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionmodel',
            name='trans_id',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
    ]
