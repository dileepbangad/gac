from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.response import Response
from rest_framework.authentication import get_authorization_header
from .models import *
from rest_framework.views import APIView
from Students.authentication import decode_access_token
from .models import *
from Students.models import *


class BooksViewAPI(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            books = []
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            for book in Book.objects.filter():
                books.append({
                    "title":book.title,
                    "content":book.content.url,
                })
            return Response({
                "data":books,
            })

        raise AuthenticationFailed('unauthenticated')

class NotesViewAPI(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            Notes = []
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            for note in Note.objects.filter():
                Notes.append({
                    "category":note.category,
                    "title":note.title,
                    "content":note.content.url,
                })
            return Response({
                "data":Notes,
            })

        raise AuthenticationFailed('unauthenticated')

class LectureViewAPI(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            lectures = []
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            for lecture in Lecture.objects.filter():
                lectures.append({
                    "title":lecture.title,
                    "link":lecture.link,
                })
            return Response({
                "data":lectures,
            })

        raise AuthenticationFailed('unauthenticated')

class PaperViewAPI(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            papers = []
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            for paper in ExamPaper.objects.filter():
                papers.append({
                    "subject":paper.subject,
                    "year":paper.year,
                    "content":paper.paper.url,
                })
            return Response({
                "data":papers,
            })

        raise AuthenticationFailed('unauthenticated')