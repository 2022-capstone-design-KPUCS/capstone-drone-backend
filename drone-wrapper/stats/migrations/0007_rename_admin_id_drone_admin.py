# Generated by Django 4.0.2 on 2022-04-02 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0006_alter_drone_admin_id_alter_drone_flight_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drone',
            old_name='admin_id',
            new_name='admin',
        ),
    ]