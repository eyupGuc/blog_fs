
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from .models import Category, Blog
from .serializers import CategorySerializer,BlogSerializer
from .permissions import IsAdminReadOnly


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminReadOnly]
    filterset_fields = ['name']


class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filterset_fields = ['category']
    search_fields = ['title','content']
