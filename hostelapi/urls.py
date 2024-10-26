from rest_framework_nested import routers
from django.conf import settings  # new
from django.conf.urls.static import static  # new
from . import views

router = routers.DefaultRouter()
router.register('student', views.StudentViewSet, basename='student')
router.register('room', views.RoomViewSet, basename='room')
router.register('booking', views.BookingViewSet, basename='booking')
router.register('payment', views.PaymentViewSet, basename='payment')

# router.register('item', views.ItemViewSet, basename='item')


urlpatterns = router.urls 

