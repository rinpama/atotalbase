# Generated by Django 4.0.4 on 2022-05-10 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_asset', '0003_document_title_alter_document_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='upload',
            field=models.FileField(default='', upload_to='document/'),
        ),
    ]