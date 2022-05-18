from rest_framework import serializers


class PickRequestSerializers(serializers.Serializer):
    lines = serializers.ListField()
