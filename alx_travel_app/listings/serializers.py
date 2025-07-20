from rest_framework import serializers

class ListingSerializer(serializers.Serializer):
    title = serializers.CharField()

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title is required.")
        return value
