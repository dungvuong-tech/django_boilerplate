from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing user instances.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
