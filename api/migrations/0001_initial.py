# Generated by Django 4.2.6 on 2023-12-14 11:44

import api.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.CharField(default=api.models.generate_unique_id, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('is_team_manager', models.BooleanField(default=False)),
                ('country', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('rule', models.CharField(choices=[('Chef de délégation', 'Chef de délégation'), ('Jury / Organisme de contrôle', 'Jury / Organisme de contrôle'), ('Media', 'Media')], default='Chef de délégation', max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.CharField(default=api.models.generate_unique_id, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('photo', models.TextField()),
                ('category', models.CharField(choices=[('Haute Personnalité', 'Haute Personnalité'), ('Invité', 'Invité'), ('Jury et organisme de contrôle', 'Jury et organisme de contrôle'), ('Délégation', 'Délégation'), ('Organisation', 'Organisation'), ('Presse', 'Presse'), ('Radio télé difiseur', 'Radio télé difiseur'), ('Bénévole', 'Bénévole')], max_length=50)),
                ('function', models.CharField(choices=[('Haute Personnalité', 'Haute Personnalité'), ('Invité', 'Invité'), ('Président du jury', 'Président du jury'), ('Délégation technique sportif', 'Délégation technique sportif'), ('Officiel sport', 'Officiel sport'), ('Juré culturel', 'Juré culturel'), ('Antidopage', 'Antidopage'), ('Officiel', 'Officiel'), ('Membre du gouvernement', 'Membre du gouvernement'), ('Chef de délégation', 'Chef de délégation'), ('Chef de mission', 'Chef de mission'), ('Administrateif', 'Administrateif'), ('Entraîneur', 'Entraîneur'), ('Technique', 'Technique'), ('Médical', 'Médical'), ('Compétiteur', 'Compétiteur'), ('CNJF', 'CNJF'), ('Officile-Org', 'Officile-Org'), ('CIJF', 'CIJF'), ('Responsable de site', 'Responsable de site'), ("Reponsable d'activité", "Reponsable d'activité"), ('Sécurité', 'Sécurité'), ('Organisateur', 'Organisateur'), ('Presse', 'Presse'), ('Média télé-radio', 'Média télé-radio'), ('Bénévole', 'Bénévole')], max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('activity', models.CharField(max_length=50)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
