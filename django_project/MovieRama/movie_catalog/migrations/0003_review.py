# Generated by Django 3.0.5 on 2020-07-04 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie_catalog', '0002_auto_20200702_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(choices=[('L', 'likes'), ('H', 'hates')], max_length=1)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movie_catalog.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'movie')},
            },
        ),
    ]
