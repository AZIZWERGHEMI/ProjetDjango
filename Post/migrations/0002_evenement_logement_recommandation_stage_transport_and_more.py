# Generated by Django 5.0.2 on 2024-05-08 17:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Post.post')),
                ('date_evenement', models.DateField()),
                
            ],
            bases=('Post.post',),
        ),
        migrations.CreateModel(
            name='Logement',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Post.post')),
                ('localisation', models.CharField(max_length=200)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contact_info', models.CharField(max_length=200)),
            ],
            bases=('Post.post',),
        ),
        migrations.CreateModel(
            name='Recommandation',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Post.post')),
                ('texte', models.TextField()),
            ],
            bases=('Post.post',),
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Post.post')),
                ('localisation', models.CharField(max_length=200)),
                ('societe', models.CharField(max_length=200)),
                ('duree', models.IntegerField()),
                ('sujet', models.CharField(max_length=200)),
                ('specialite', models.CharField(max_length=200)),
            ],
            bases=('Post.post',),
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Post.post')),
                ('destination', models.CharField(max_length=200)),
                ('type_transport', models.CharField(max_length=100)),
                ('contact_info', models.CharField(max_length=200)),
            ],
            bases=('Post.post',),
        ),
        migrations.RenameField(
            model_name='likes',
            old_name='utilisateur',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='utilisateur',
            new_name='user',
        ),
        migrations.CreateModel(
            name='EvenClub',
            fields=[
                ('evenement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Post.evenement')),
                ('prixC', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=100)),
                ('domaine', models.CharField(max_length=100)),
            ],
            bases=('Post.evenement',),
        ),
        migrations.CreateModel(
            name='EvenSocial',
            fields=[
                ('evenement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Post.evenement')),
                ('prixS', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=100)),
                ('theme', models.CharField(max_length=100)),
            ],
            bases=('Post.evenement',),
        ),
    ]
