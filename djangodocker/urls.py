from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from djangodocker.viewset import ViewSet
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
router = routers.DefaultRouter()
router.register(r'users', ViewSet.UserViewSet)
router.register(r'blogs', ViewSet.BlogViewSet)

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'^docs/', schema_view, name="docs"),
	url('accounts/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api/', include(router.urls)),
	url(r'^auth_token/', obtain_jwt_token),
	url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^admin/', admin.site.urls),
	url(r'^ueditor/', include('DjangoUeditor.urls' )),
]

