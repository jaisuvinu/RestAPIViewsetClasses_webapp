
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from student import views

'''
#method1:
---------
#Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi',views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
'''
'''
#method2:
#---------

#Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi',views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
'''

#method3:
#---------

#Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi',views.StudentReadOnlyModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
