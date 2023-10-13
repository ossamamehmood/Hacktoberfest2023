from django import urls
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import article_list, article_detail, ArticleViewAPI, ArticleDetails, GenericApiView, LocationsView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    # path('viewset/',include(router.urls)),
    # path('viewset/<int:pk>/',include(router.urls)),
    path('article/', ArticleViewAPI.as_view()),
    path('location/<int:id>/', LocationsView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericApiView.as_view()),
]
 