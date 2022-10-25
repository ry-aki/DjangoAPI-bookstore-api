from rest_framework import serializers
from Bookstore.models import BookModel
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'
