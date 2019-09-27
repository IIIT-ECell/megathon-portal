# Generated by Django 2.2.5 on 2019-09-27 22:36

from django.db import migrations, models
import portal.models
import portal.validators


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20190928_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='presentation',
            field=models.FileField(blank=True, null=True, upload_to=portal.models.get_upload_path, validators=[portal.validators.FileValidator(content_types=('application/pdf', 'application/vnd.ms-powerpoint', 'application/vnd.ms-powerpoint', 'application/vnd.openxmlformats-officedocument.presentationml.presentation', 'application/vnd.openxmlformats-officedocument.presentationml.slideshow'), max_size=104857600)]),
        ),
    ]
