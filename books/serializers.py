from rest_framework import serializers
from .models import Book
from authentication.models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'
    
    def get_subjects(self, obj):
        return [subject.name for subject in obj.subjects.all()]