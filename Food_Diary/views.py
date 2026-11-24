from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from Food_Diary.serializers import UserSerializer,FoodSerializer,WeightSerializer
from rest_framework import authentication, permissions
from Food_Diary.models import FoodDiaryDb,WeightTrackerDb
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class SignUp(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data={
                "message":"User Signup Successful"
            },status=201)
        return Response(data={"message":"invalid Data"},status=400)


class UserView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        qs=User.objects.all()
        serializer_instance=UserSerializer(qs,many=True)
        return Response(serializer_instance.data,status=200)


class FoodListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        form_data=request.data
        serializer_instance=FoodSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(created_by=request.user)
            return Response(
                {"message":"Food Added Successfully"},status=201)
        return Response(serializer_instance.errors,status=400)

    def get(self,request):
            qs = FoodDiaryDb.objects.filter(created_by=request.user)
            serializer_instance=FoodSerializer(qs,many=True)
            return Response(serializer_instance.data,status=200)


class FoodUpdateDeleteView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def put(self,request,id):
        food=get_object_or_404(FoodDiaryDb,id=id,created_by=request.user)
        form_data=request.data
        serializer_instance=FoodSerializer(food,data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data={
                "message":"Updated successfully"
                })
        return Response(data=serializer_instance.errors)
    def delete(self,request,id):
        food=get_object_or_404(FoodDiaryDb,id=id,created_by=request.user)
        food.delete()
        return Response(data={
            "message":"Food Deleted successfully"
        })






class WeightListView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request):
        form_data=request.data
        serializer_instance=WeightSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(created_by=request.user)
            return Response(data={
                "message":"weight added successfully"
            },status=200)
        else:
            return Response(data=serializer_instance.errors,status=400)

    def get(self,request):
        qs=WeightTrackerDb.objects.filter(created_by=request.user)
        serializer_instance=WeightSerializer(qs,many=True)
        return Response(serializer_instance.data,status=200)

class LogoutView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({
                    "message": "Logout successful"
                    },status=200)
            except TokenError:
                return Response({
                    "message": "Invalid token"
                    },status=400)
        return Response({
            "message": "Refresh token is required"
            },status=400)