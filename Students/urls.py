from django.urls import path,include
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "GLOBAL ACCESS CENTER"
admin.site.site_title = "GAC-GLOBAL ACCESS CENTER"
admin.site.index_title = "GAC-Administration"
urlpatterns = [
    path('register',RegisterAPIView.as_view()),
    path('login',LoginAPIView.as_view()),
    path('user',UserAPIView.as_view()),
    path('refresh',RefreshAPIView.as_view()),
    path('logout',LogoutAPIView.as_view()),
    path('forget',ForgetPasswordAPIView.as_view()),
    path('changepassword',ChangePasswordAPIView.as_view())
]