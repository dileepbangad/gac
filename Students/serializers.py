from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework.exceptions import APIException

class UserSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','email','gid','password','semid','section']
        # extra_kwargs ={
        #     'password':{'write_only':True}
        # }

    def create(self,validated_data):
        email = validated_data.pop('email',None)
        name = validated_data.pop('name',None)
        section = validated_data.pop("section",None)
        semester = validated_data.pop('semid',None)
        instance = self.Meta.model(**validated_data)
        if email is not None:
            if("@gitjaipur.com" not in email):
                raise APIException('please enter your college email address!')
            user = Student.objects.filter(email=email).first()
            if(user):
                raise APIException('Student Already Exist, Please Login')
            else:
                gid = gidgen(email)
                password = get_password()
                gaccredentials(name,gid,password,email)
                instance.set_password(password)
                instance.gid = gid
                instance.name = name
                instance.email = email
                instance.section = section
                instance.semid = semester
                instance.username = gid
        instance.save()
        return instance
