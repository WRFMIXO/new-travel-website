from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

from .serializers import UserSerializer
from .models import AppUsers

class LoginView(APIView):
    def post(self, request, format=None):
        # Récupérer les informations d'identification de la requête POST
        username = request.data.get('username')
        password = request.data.get('password')

        # Authentification de l'utilisateur
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Connexion de l'utilisateur si l'authentification réussit
            login(request, user)

            # Générer un jeton d'authentification (si vous en avez besoin)
            token, created = Token.objects.get_or_create(user=user)

            return Response({'success': True, 'message': 'Login successful', 'token': token.key})
        else:
            # Retourner une réponse d'erreur si l'authentification échoue
            return Response({'success': False, 'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

class CreateUserView(generics.CreateAPIView):
    queryset = AppUsers.objects.all()
    serializer_class = UserSerializer