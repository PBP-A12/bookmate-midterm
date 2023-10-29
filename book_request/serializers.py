from rest_framework import serializers
from .models import BookRequest

class BookRequestSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()
    member = serializers.SerializerMethodField()
    date_requested = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = BookRequest
        fields = '__all__'
    
    def get_subjects(self, obj):
        return [subject.name for subject in obj.subjects.all()]
    
    def get_member(self, obj):
        return obj.member.account.username