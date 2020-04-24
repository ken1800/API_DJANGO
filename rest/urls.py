
from .views import HelloApiView,HelloViewSet,UserProfileViewSet,UserLoginApiView,UserProfileFeedViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset/',HelloViewSet, basename ='hello-viewset')
router.register('profiles',UserProfileViewSet)
router.register('feed',UserProfileFeedViewSet)





urlpatterns = [
    path('proff/',HelloApiView.as_view()),
    path('login/',UserLoginApiView.as_view()),
    path('', include(router.urls)),
]




