from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserProfileSerializer

# Create your views here.
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
 
    def get_queryset(self):
        return get_user_model().objects.all().filter(username=self.request.user)