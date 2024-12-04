from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer 

# Create your views here.

# class ArticleView(viewsets.ViewSet): 
# def list(self, request): 
#   queryset = Article.objects.all() 
#   serializer = ArticleSerializer(queryset, many=True) 
#   return Response(serializer.data) 
# def retrieve(self, request, pk=None): 
#   queryset = Article.objects.all() 
#   user = get_object_or_404(queryset, pk=pk) 
#   serializer = ArticleSerializer(user) 
#   return Response(serializer.data)

class ArticleViewSet(viewsets.ModelViewSet): 
  serializer_class = ArticleSerializer 
  queryset = Article.objects.all()