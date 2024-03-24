from django.db import models



class Deck(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    user_creator = models.CharField(max_length=255)
    deck_size = models.IntegerField()
    date_update = models.DateTimeField()
    

class MTG_Card(models.Model):
    name = models.CharField(max_length=255)
    card_type = models.CharField(max_length=255)
    image_path = models.CharField(max_length=300)
    images = models.JSONField()
    booster = models.BooleanField(),
    cardmarketID = models.IntegerField()
    colors = models.JSONField()
    color_identity = models.JSONField()
    edhrec_rank = models.IntegerField()
    flavor_text = models.TextField()
    foil = models.BooleanField()
    nonfoil = models.BooleanField()
    promo = models.BooleanField()
    keywords = models.JSONField()
    legalities = models.JSONField()
    lang = models.CharField(max_length=10)
    mana_cost = models.CharField(max_length=20)
    power = models.IntegerField()
    toughness = models.IntegerField()
    preview = models.JSONField()
    prices = models.JSONField()
    rarity = models.CharField(max_length=20)
    reprint = models.BooleanField()
    rulings_uri = models.CharField(max_length=255)
    scryfall_uri = models.CharField(max_length=255)
    set_card = models.CharField(max_length=4)
    type_line = models.CharField(max_length=255)
    variation = models.BooleanField()
    released_at = models.TimeField()
    collector_number = models.IntegerField()

class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete = models.CASCADE)
    card = models.ForeignKey(MTG_Card, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)