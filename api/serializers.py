from rest_framework.serializers import ModelSerializer
from .models import *

class UserListSerializer(ModelSerializer):
    class Meta:
        model = UserList
        fields = "__all__"