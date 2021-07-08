from rest_framework import serializers

from core.models import Game

class GamesScoreSerializer(serializers.ModelSerializer):
    """Serializer for the games score object"""

    class Meta:
        model = Game
        fields = '__all__'

    def update(self, instance, validated_data):
        """Update games score for a user"""
        games_score = super().update(instance, validated_data)
        games_score.save()

        return games_score
