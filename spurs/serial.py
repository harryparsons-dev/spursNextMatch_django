from rest_framework import routers, serializers, viewsets
from .models import match


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = match
        fields = ["id", "team", "venue", "date" ]
