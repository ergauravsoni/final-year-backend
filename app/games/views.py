from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.models import Token

from games.serializers import GamesScoreSerializer
from core.models import Game

class ListGameScoreView(generics.ListAPIView):
    """List View for games score object"""
    serializer_class = GamesScoreSerializer
    authentication_classes = {authentication.TokenAuthentication, }
    permission_classes = {permissions.IsAuthenticated, }

    def get_queryset(self):
        """Retrieve and return authentication user game object"""
        return Game.objects.filter(user=Token.objects.get(key=str(self.request.META.get('HTTP_AUTHORIZATION'))[6:]).user)


class CreateGameScoreView(generics.CreateAPIView):
    """Create View for games score object"""
    serializer_class = GamesScoreSerializer
    authentication_classes = {authentication.TokenAuthentication, }
    permission_classes = {permissions.IsAuthenticated, }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user

class ManageGameScoreView(generics.RetrieveUpdateAPIView):
    """Manage View for games score object"""
    serializer_class = GamesScoreSerializer
    authentication_classes = {authentication.TokenAuthentication, }
    permission_classes = {permissions.IsAuthenticated, }

    def perform_update(self, serializer):
        instance = serializer.save(user=self.request.user)

    def get_object(self):
        """Retrieve and return authentication user game object"""
        return Game.objects.get(user=Token.objects.get(key=str(self.request.META.get('HTTP_AUTHORIZATION'))[6:]).user)
