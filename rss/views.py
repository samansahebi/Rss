from rest_framework import pagination, views, generics, status
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer, RssSerializer


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = pagination.PageNumberPagination


class AddRss(views.APIView):
    def post(self, request):
        serializer = RssSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

