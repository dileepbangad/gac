from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.response import Response
from rest_framework.authentication import get_authorization_header
from .models import *
from rest_framework.views import APIView
from Students.authentication import decode_access_token
from .models import *
from Students.models import *


class ScheduledLectureAPI(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            semid = user.semid
            section = user.section
            lecture = Lecture.objects.get(semid=semid,section=section)
            return Response({
                "section":lecture.section,
                "updateDate":lecture.updateDate,
                "link":lecture.schedule.url,
            })

        raise AuthenticationFailed('unauthenticated')
