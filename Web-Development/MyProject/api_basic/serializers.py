from django.db.models import fields
from rest_framework import serializers
from .models import Article, Location,Student


class ArticleSerializer(serializers.ModelSerializer):
   class Meta:
       model = Article
       fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'