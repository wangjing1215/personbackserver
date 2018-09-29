# coding: utf-8
from account.models import User
from blog.models import Article

from rest_framework import  serializers
# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id',
				  'username',
                  'email',
                  'is_staff',
                  )
class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ('title',
				  'category',
				  'jianshu',
				  'content',
				  )