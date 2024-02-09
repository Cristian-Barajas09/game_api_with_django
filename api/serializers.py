"""Response and Request for this app"""
from dataclasses import dataclass
from rest_framework import serializers
from api.models import (
    Game,
    GameDeveloper
)

class GameSerializer(serializers.ModelSerializer):
    """Response and Request for game model"""

    published_at = serializers.DateTimeField(required=False)
    discount = serializers.DecimalField(max_digits=5,decimal_places=2,required=False)

    @dataclass
    class Meta:
        """info for Serializer"""
        model = Game
        fields = [
            'title',
            'price',
            'discount',
            'published_at'
        ]

class GameDeveloperSerializer(serializers.ModelSerializer):
    """Response and Request for game developer model"""
    oficial_page = serializers.URLField(required=False)
    added_at = serializers.DateTimeField(required=False,format="%Y-%m-%d")
    created_at = serializers.DateField(required=False)

    @dataclass
    class Meta:
        """info for Serializer"""
        model = GameDeveloper
        fields = [
            'name',
            'oficial_page',
            'added_at',
            'created_at',
        ]
