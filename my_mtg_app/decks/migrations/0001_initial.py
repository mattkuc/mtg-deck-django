# Generated by Django 5.0.3 on 2024-03-24 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('user_creator', models.CharField(max_length=255)),
                ('deck_size', models.IntegerField()),
                ('date_update', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MTG_Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('card_type', models.CharField(max_length=255)),
                ('image_path', models.CharField(max_length=300)),
                ('images', models.JSONField()),
                ('cardmarketID', models.IntegerField()),
                ('colors', models.JSONField()),
                ('color_identity', models.JSONField()),
                ('edhrec_rank', models.IntegerField()),
                ('flavor_text', models.TextField()),
                ('foil', models.BooleanField()),
                ('nonfoil', models.BooleanField()),
                ('promo', models.BooleanField()),
                ('keywords', models.JSONField()),
                ('legalities', models.JSONField()),
                ('lang', models.CharField(max_length=10)),
                ('mana_cost', models.CharField(max_length=20)),
                ('power', models.IntegerField()),
                ('toughness', models.IntegerField()),
                ('preview', models.JSONField()),
                ('prices', models.JSONField()),
                ('rarity', models.CharField(max_length=20)),
                ('reprint', models.BooleanField()),
                ('rulings_uri', models.CharField(max_length=255)),
                ('scryfall_uri', models.CharField(max_length=255)),
                ('set_card', models.CharField(max_length=4)),
                ('type_line', models.CharField(max_length=255)),
                ('variation', models.BooleanField()),
                ('released_at', models.TimeField()),
                ('collector_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decks.deck')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decks.mtg_card')),
            ],
        ),
    ]
