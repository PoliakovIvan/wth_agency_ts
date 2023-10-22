from django.contrib.auth.models import User, Team
from rest_framework import viewsets
from rest_framework import permissions
from apps.teamapi.serializers import UserSerializer, TeamSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

       


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]


