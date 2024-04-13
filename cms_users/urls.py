from django.urls import path
from .views import LoginView, CreateUserView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', CreateUserView.as_view(), name='register'),
    # Ajoutez d'autres URLs de votre application ici si nécessaire
]
