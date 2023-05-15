from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import APIException, AuthenticationFailed
from .serializers import UserSerializer
from .models import *
from .authentication import *


# Create your views here.
class RegisterAPIView(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)

class LoginAPIView(APIView):
    def post(self,request):
        user = Student.objects.filter(gid = request.data['gid']).first()
        if not user:
            raise APIException('Invalid Credentials')
        
        if not user.check_password(request.data['password']):
            raise APIException('Invalid Credentials')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()
        response.set_cookie(key='refreshToken',value=refresh_token,httponly=True)
        response.data = {
            'token':access_token,
            'refreshToken':refresh_token
        }

        return response

class ForgetPasswordAPIView(APIView):
    def post(self,request):
        user = Student.objects.filter(email = request.data['email']).first()
        if not user:
            raise APIException("Invalid User")
        password = get_password()
        name = user.name
        gid = user.gid
        email = user.email
        gaccredentials(name, gid, password, email)
        instance = user
        instance.set_password(password)
        instance.save()
        return Response({
                'msg':"Success"
        })

class ChangePasswordAPIView(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            password = request.data['password']
            instance = user
            instance.set_password(password)
            instance.save()
            return Response({
                'msg':"Password Change Sucessfully"
            })

class UserAPIView(APIView):
    def get(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()

            return Response({
                'id':id,
                "gid":user.gid,
                "name":user.name,
                "email":user.email,
                "semid":user.semid,
                "section":user.section
            })

        raise AuthenticationFailed('unauthenticated')

class RefreshAPIView(APIView):
    def post(self,request):
        refresh_token = request.COOKIES.get('refreshToken')
        print(refresh_token)
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response({
            'token':access_token
        })

class LogoutAPIView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie(key= "refreshToken")
        response.data = {
            'message':'success'
        }
        return response

