from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views
from django.urls import path, include

from portal.views import Signup, UserRetrieve

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', Signup.as_view(), name="signup"),
    path('updations/', UserRetrieve.as_view(), name="updations"),


]
