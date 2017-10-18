from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

from . import views

schema_view = get_schema_view(title='Pastebin API')

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users',views.UserViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^schema/$',schema_view),
]

