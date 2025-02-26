from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import User
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.schemas import AutoSchema

# Create your views here.

# Create a custom permission
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to authenticated users
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the user themselves or staff
        return obj == request.user or request.user.is_staff

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users.
    Provides CRUD operations: GET (list & detail), POST, PUT, PATCH, DELETE
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['username', 'email', 'password'],
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Unique username'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, format='email', description='Valid email address'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, format='password', description='Strong password'),
            'first_name': openapi.Schema(type=openapi.TYPE_STRING),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING),
            'country': openapi.Schema(type=openapi.TYPE_STRING),
            'main_city': openapi.Schema(type=openapi.TYPE_STRING),
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING),
            'user_type': openapi.Schema(type=openapi.TYPE_STRING, enum=['regular', 'organizer']),
        }
    ),
    responses={
        201: UserSerializer,
        400: "Bad Request - Invalid data"
    },
    operation_description="Register a new user account"
)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_user(request):
    """
    Register a new user and return a response.
    
    This endpoint is publicly accessible and allows new users to create an account.
    After registration, users can obtain a JWT token using the /api/token/ endpoint.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
