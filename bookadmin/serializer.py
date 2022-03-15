
from rest_framework import serializers
# from rest_framework import BookAdmin
from .models import BookAdmin

class BookAdminserializer(serializers.ModelSerializer):
    class Meta:
        model = BookAdmin
        fields = "__all__"