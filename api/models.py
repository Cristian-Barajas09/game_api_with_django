"""models for this app"""
import decimal
from django.db import models
from django.utils import timezone
from datetime import date
# Create your models here.

class Game(models.Model):
    """Game Model class"""
    title = models.CharField(max_length=255)

    price = models.DecimalField(decimal_places=2,max_digits=5,default=0)
    discount = models.DecimalField(decimal_places=2,max_digits=5,default=0)
    created_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    games = models.ForeignKey(
        'api.Game',
        related_name = 'game',
        on_delete = models.CASCADE,
        null=True
    )

    def soft_delete(self):
        """soft deleted"""
        self.deleted_at = timezone.now()
        self.save()


    def apply_discount(self) -> decimal.Decimal:
        """apply discount for this game"""
        return self.price * self.discount / 100

    def publish(self):
        """publish game"""
        self.published_at = True
        self.save()



class GameDeveloper(models.Model):
    """Game developer class"""
    name = models.CharField(max_length=255,default="Indie")
    created_at = models.DateField(default=date.today())
    added_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    oficial_page = models.URLField(null=True)

    def soft_delete(self):
        """soft deleted"""
        self.deleted_at = timezone.now()
        self.save()


class ShoppingCar(models.Model):
    """shopping car for users"""

class Comment(models.Model):
    """comment for the game"""

class Like(models.Model):
    """like for the game"""
