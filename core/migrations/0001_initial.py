# Generated by Django 3.2.8 on 2021-11-14 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('total_seats', models.IntegerField()),
                ('city', models.TextField(choices=[('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Hyderabad', 'Hyderabad'), ('Chennai', 'Chennai')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'db_table': 'cinema',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.IntegerField()),
                ('release_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'db_table': 'movie',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.movie')),
            ],
            options={
                'db_table': 'showtime',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_seats', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.showtime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'reservation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CinemaSeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_seats', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.showtime')),
            ],
            options={
                'db_table': 'cinema_seat',
                'managed': True,
            },
        ),
    ]
