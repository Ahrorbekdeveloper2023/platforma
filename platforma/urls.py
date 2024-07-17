from django.urls import path, include

from .views import (KursModelViewSet, DarsModelViewSet, VideoModelViewSet,
                    CommentModelViewSet, EmailModelViewSet, LikeAPIView, LikeCreateViewSet)

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers


router = routers.SimpleRouter()
router.register('kurs', KursModelViewSet)
router.register('dars', DarsModelViewSet)
router.register('video', VideoModelViewSet)
router.register('comment', CommentModelViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/email/', EmailModelViewSet.as_view()),
    path('api/v1/like/<int:pk>/', LikeAPIView.as_view()),
    path('api/v1/like/create/', LikeCreateViewSet.as_view()),


    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api-auth/', include('rest_framework.urls')),

    path('api/v1/', include('rest_registration.api.urls')),
]