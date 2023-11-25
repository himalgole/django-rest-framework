from rest_framework import serializers

from .models import Student

class ApisSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Student
        fields = "__all__"