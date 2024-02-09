# Generated by Django 5.0.2 on 2024-02-09 01:32

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_game_discount_alter_game_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='games',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game', to='api.game'),
        ),
        migrations.AddField(
            model_name='game',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='gamedeveloper',
            name='added_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='gamedeveloper',
            name='created_at',
            field=models.DateField(default=datetime.date(2024, 2, 8)),
        ),
        migrations.AddField(
            model_name='gamedeveloper',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='gamedeveloper',
            name='name',
            field=models.CharField(default='Indie', max_length=255),
        ),
        migrations.AddField(
            model_name='gamedeveloper',
            name='oficial_page',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='gamedeveloper',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
