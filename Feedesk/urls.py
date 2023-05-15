from django.urls import path,include
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "GLOBAL ACCESS CENTER"
admin.site.site_title = "GAC-GLOBAL ACCESS CENTER"
admin.site.index_title = "GAC-Administration"
urlpatterns = [
   path("feeDetail/",FeeReportViewAPI().as_view()),
   path("feeTransaction/",FeeTransactionViewAPI().as_view()),
]