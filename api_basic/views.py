from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing all articles.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

      if id:
        return self.retrieve(request)

      else:
        return self.list(request)

    def post(self, request):
      return self.create(request)

    def put(self, request, id=None):
      return self.update(request, id)

    def delete(self, request, id):
      return self.destroy(request, id)