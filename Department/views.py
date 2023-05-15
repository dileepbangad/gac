from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.response import Response
from rest_framework.authentication import get_authorization_header
from .models import *
from rest_framework.views import APIView
from Students.authentication import decode_access_token
from .models import *
from Students.models import *


class DepartmentViewAPI(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            faculties = []
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            for faculty in Faculty.objects.filter():
                faculties.append({
                    "department":faculty.department,
                    "name":faculty.name,
                    "designation":faculty.designation,
                    "qualification":faculty.qualification,
                    "research":faculty.research,
                    "email":faculty.email,
                    "photo":faculty.photo.url,
                })
            return Response({
                "data":faculties,
            })

        raise AuthenticationFailed('unauthenticated')