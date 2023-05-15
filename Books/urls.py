from django.urls import path,include
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "GLOBAL ACCESS CENTER"
admin.site.site_title = "GAC-GLOBAL ACCESS CENTER"
admin.site.index_title = "GAC-Administration"
urlpatterns = [
   path("books/",BooksViewAPI.as_view()),
   path("notes/",NotesViewAPI.as_view()),
   path("paper/",PaperViewAPI.as_view()),
   path("lecture/",LectureViewAPI.as_view()),
]