from django.urls import path
from .views import ListMediaContentView, ListTextContentView, CreateMediaContentView, CreateTextContentView

urlpatterns = [
    path('textcontent/create/', CreateTextContentView.as_view(), name='create-text-content'),
    path('textcontent/list/', ListTextContentView.as_view(), name='list-text-content'),
    path('mediacontent/create/', CreateMediaContentView.as_view(), name='create-media-content'),
    path('mediacontent/list/', ListMediaContentView.as_view(), name='list-media-content'),
]