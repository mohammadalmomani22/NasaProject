from rest_framework import serializers

class SeismicDataRequestSerializer(serializers.Serializer):
    from_date = serializers.DateField(format='%Y-%m-%d', input_formats=['%Y-%m-%d'])
    to_date = serializers.DateField(format='%Y-%m-%d', input_formats=['%Y-%m-%d'])
