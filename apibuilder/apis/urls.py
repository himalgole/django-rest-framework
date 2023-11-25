from django.urls import include, path
# import routers
from rest_framework import routers
 
# import everything from views
from . import views
router = routers.DefaultRouter()
 
# define the router path and viewset to be used
router.register(r'apis',views.ApisViewSet)
 
# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('apis/', include('rest_framework.urls'))
]