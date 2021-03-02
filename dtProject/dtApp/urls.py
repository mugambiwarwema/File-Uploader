


from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

router.register(r'userprofile', views.UserProfile_ViewSet)


urlpatterns = [
    path('api/', include(router.urls))
]