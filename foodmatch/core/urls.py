from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, DonorViewSet, NGOViewSet, FoodItemViewSet, FoodRequestViewSet

router = DefaultRouter()
router.register(r'donors', DonorViewSet)
router.register(r'ngos', NGOViewSet)
router.register(r'food-items', FoodItemViewSet)
router.register(r'food-requests', FoodRequestViewSet)
router.register(r'users', UserViewSet)  # ✅ Now you can create users via API


urlpatterns = [
    path('', include(router.urls)),
]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet, DonorViewSet, NGOViewSet

# # router = DefaultRouter()
# # router.register(r'users', UserViewSet)  # ✅ Now you can create users via API
# # router.register(r'donors', DonorViewSet)
# # router.register(r'ngos', NGOViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]
