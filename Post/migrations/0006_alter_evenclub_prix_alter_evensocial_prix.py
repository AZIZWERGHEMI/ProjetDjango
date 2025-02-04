# Generated by Django 5.0.2 on 2024-05-09 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0005_remove_evenement_prix_evenclub_prix_evensocial_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenclub',
            name='prix',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='evensocial',
            name='prix',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True),
        ),
    ]
