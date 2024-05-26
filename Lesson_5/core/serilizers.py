from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def validate(self, attrs):
        if attrs['likes'] < 0:
            raise ValidationError("Кол-во лайков должно быть положительно кол-во")
        return attrs