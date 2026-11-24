from rest_framework import serializers
from django.contrib.auth.models import User
from Food_Diary.models import FoodDiaryDb,WeightTrackerDb

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model=FoodDiaryDb
        fields="__all__"
        read_only_fields=["id","created_by","created_at","updated_at"]


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model=WeightTrackerDb
        fields="__all__"
        read_only_fields=["id","created_by","created_at","updated_at"]
        