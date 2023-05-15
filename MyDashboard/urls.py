from django.urls import path,include
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "GLOBAL ACCESS CENTER"
admin.site.site_title = "GAC-GLOBAL ACCESS CENTER"
admin.site.index_title = "GAC-Administration"
urlpatterns = [
    path("assignments/",AssignmentListAPI.as_view()), #AssignmentListAPI
    path("dashboard/",DashBoardContentAPI.as_view()),
    path("profileData/",ProfileViewAPI.as_view()),
    # path("submission/",views.submission), #SubmissionAPI
    path("progressList/",ProgressReportAPI.as_view()), #progressreportAPI
    path("attendanceList/",AttendanceReportAPI.as_view()),#attendencereportAPI
    # path("eventList/",views.event_list),#eventListAPI
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
     