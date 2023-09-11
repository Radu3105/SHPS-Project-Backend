from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return Response({'access_token': access_token}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUserByTokenView(APIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        print(user)
        if user and user.is_authenticated:
            return Response({
                'user_id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'date_of_birth': user.date_of_birth,
                'gender': user.gender,
                'weight': user.weight,
                'height': user.height,
                'phone_number': user.phone_number,
                'geolocation': user.geolocation,
                'date_joined': user.date_joined,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Authentication failed'}, status=status.HTTP_400_BAD_REQUEST)
    