# Generated by Django 4.1.1 on 2022-10-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_certificate_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_link',
            field=models.URLField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Upload'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='.imgs/default -image.jpg', null=True, upload_to=''),
        ),
    ]
