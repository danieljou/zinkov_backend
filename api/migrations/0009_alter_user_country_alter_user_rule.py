# Generated by Django 4.2.6 on 2023-11-29 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_participant_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(default='Camaroon', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='rule',
            field=models.CharField(choices=[('Chef de délégation', 'Chef de délégation'), ('Jury / Organisme de contrôle', 'Jury / Organisme de contrôle'), ('Media', 'Media')], default='Chef de délégation', max_length=50),
        ),
    ]
