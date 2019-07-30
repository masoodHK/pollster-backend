from .serializers import PollsSerializer, OptionsSerializer, CommentsSerializer
from rest_framework import generics, mixins
from .models import Poll, Option, Comments

# Create your views here.
class PollsView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = PollsSerializer

    def get_queryset(self):
        return Poll.objects.all()

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)

class PollsRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollsSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset

class OptionsView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = OptionsSerializer

    def get_queryset(self):
        return Option.objects.filter(poll_id=self.kwargs['poll_id'])

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class OptionsRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionsSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset

class CommentsRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset

class CommentsView(generics.ListAPIView):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        return Comments.objects.filter(poll=self.kwargs['poll_id'])

    def post(self, request, *args, **kwargs):
        pass
