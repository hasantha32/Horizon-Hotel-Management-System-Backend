# Generated by Django 4.2.20 on 2025-03-18 08:25

import django.utils.timezone
from django.db import migrations, models


def create_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")

    # Define the groups you want to create
    groups = ["super_user", "customer"]

    # Create the groups if they do not exist
    for group_name in groups:
        Group.objects.get_or_create(name=group_name)


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('date_of_birth', models.DateField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_groups', to='auth.group')),
                ('user_permissions',
                 models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(create_groups),
    ]
