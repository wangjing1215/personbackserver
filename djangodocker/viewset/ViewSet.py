# coding: utf-8
from account.models import User
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from blog.models import Article
from rest_framework import  viewsets
from djangodocker.serializers import Serializer
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class UserViewSet(viewsets.ModelViewSet):
    '''
    王晶
    '''
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = Serializer.UserSerializer

    @action(detail=False, methods=['post'], url_path='changepwd')
    def changepwd(self, request, *args, **kwargs):
        """
        修改密码
        """
        pass
class BlogViewSet(viewsets.ModelViewSet):
    '''
    王晶
    '''
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = Serializer.BlogSerializer
