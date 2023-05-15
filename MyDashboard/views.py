from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.response import Response
from rest_framework.authentication import get_authorization_header
from .models import *
from rest_framework.views import APIView
from Students.authentication import decode_access_token

from django.db.models import Q
from datetime import date


from .models import *
from Students.models import *
from Feedesk.models import *
import random
import string
from random import randint
import datetime
import calendar

class DashBoardContentAPI(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            gid = user.gid
            semid = user.semid
            section= user.section
            name = user.name
            profile = Profile_Detail.objects.get(gid=gid)
            today = datetime.date.today()
            year = today.year
            month = today.month
            totalDays = calendar.monthrange(year,month)[1]
            holiDays = sum(1 for week in calendar.monthcalendar(year, month) if week[-1])+ sum(1 for week in calendar.monthcalendar(year,month) if week[-2])
            total_assignment = Assignment.objects.filter(semid=semid,section=section).count()
            pending_assignment = Submission.objects.filter(gid=gid,submission_status='pending').count()
            FeeDetail = FeeReport.objects.filter(gid=gid).first()
            dueFee = FeeDetail.TotalDueFee
            
            return Response({
                "gid":gid,
                "name":name,
                'profile_pic':profile.profile_pic.url,
                "aggCGPA":profile.Aggregate,
                'workingDays':totalDays-holiDays,
                'totalDays':totalDays,
                'totalAssign':total_assignment,
                'pendAssign':pending_assignment,
                'dueFee':dueFee
            })

        raise AuthenticationFailed('unauthenticated')


class ProfileViewAPI(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            gid = user.gid
            profile = Profile_Detail.objects.get(gid=gid)
            
            return Response({
                "contact":profile.contact_no,
                "father_name":profile.father_name,
                "father_contact":profile.father_contact_no, 
                "dob":profile.dob, 
                "gender":profile.gender,
                "personal_email":profile.personal_email,
                "address":profile.address,
                "college_name":profile.college_name,
                "course_enrolled":profile.course_enrolled,
                "enrollment_no":profile.enrollment_no,
                "x":profile.x,
                "xii":profile.xii,
                "sem1":profile.sem1, 
                "sem2":profile.sem2, 
                "sem3":profile.sem3,
                "sem4":profile.sem4,
                "sem5":profile.sem5,
                "sem6":profile.sem6,
                "sem7":profile.sem7,
                "sem8":profile.sem8,
                "Aggregate":profile.Aggregate, 
            })

        raise AuthenticationFailed('unauthenticated')




class AssignmentListAPI(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            gid = user.gid
            assignmentlist = []
            semid = user.semid
            section = user.section
            for assignment in Assignment.objects.filter(semid=semid,section=section):
                message = {'id':assignment.id,'subject':assignment.subject,'start_date':assignment.sDate,'end_date':assignment.eDate,'title':assignment.title,'assigned':assignment.Assigned.url}
                assignmentlist.append(message)
                try:
                    submission = Submission.objects.get(assignmentId = assignment.id)
                except:
                    new_submission = Submission.objects.create(assignmentId=assignment.id,gid=gid,submitted="",submission_status="pending")

            total_assignment = Submission.objects.filter(gid=gid).count()
            pending_assignment = Submission.objects.filter(gid=gid,submission_status='pending').count()
            print("total Assignment:",total_assignment)
            print("pending Assignment:",pending_assignment)

            if len(assignmentlist)>0:
                return Response({
                    'data':assignmentlist,'total_assignment':total_assignment,'pending_assignment':pending_assignment
                })
            else:
                return Response({
                    'msg':'No Data Available'
                })
        
        raise AuthenticationFailed('unauthenticated')


class SubmitAssignmentAPI(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            gid = user.gid
            assignmentid = request.data['assignId']
            submitted = request.data['submitted']
            submission_date = date.today()
            semid = user.semid
            assignment = Assignment.objects.get(id=assignmentId)
            endDate = assignment.eDate
            if (endDate < submission_date):
                submission_status = "Late"
            else:
                submission_status = "In Time"

                
            if submitted != "":
                for submission in Submission.objects.filter(assignmentId=assignmentId, gid=gid):
                    submission.submitted = submitted
                    submission.submission_status = submission_status
                    submission.submission_date = submission_date
                    submission.save()
                return Response({
                'msg':"submission sucessfully"
             })
            else:
                return Response({
                    'msg':'please upload the document'
                })
            
        
        raise AuthenticationFailed('unauthenticated')


# #SubmissionAPI
# @csrf_exempt
# def submission(request):
#     if request.method == "POST":
#         assignmentlist = []
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         data = JSONParser().parse(stream)
#         assignmentId = data['assignmentId']
#         gid = data['gid']
#         submitted = data['submitted']
#         submission_date = date.today()
#         assignment = Assignment.objects.get(id=assignmentId)
#         endDate = assignment.eDate
#         if (endDate < submission_date):
#             submission_status = "Late"
#         else:
#             submission_status = "In Time"

#         if submitted != "":
#             for submission in Submission.objects.filter(assignmentId=assignmentId, gid=gid):
#                 submission.submitted = submitted
#                 submission.submission_status = submission_status
#                 submission.submission_date = submission_date
#                 submission.save()
#             message = {'msg':"submission sucessfully"}
#             json_data = JSONRenderer().render(message)
#             return HttpResponse(json_data,content_type='application/json')
#         else:
#             message = {'msg':'please upload the document'}
#             json_data = JSONRenderer().render(message)
#             return HttpResponse(json_data,content_type='application/json')

#progress_reportAPI
class ProgressReportAPI(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            gid = user.gid
            email = user.email
            bc = email[5:7].upper()
            mid1 =[]
            mid2 =[]
            rtu = []
            subCodelist = []
            subNamelist = []
            semid = request.data['semid']
            for subjects in Semester_wise_subject.objects.filter(semid=semid,branch_code=bc):
                sid = subjects.id
                subName = subjects.subject_name
                subCode = subjects.subject_code
                
                for reports in Progress_Report.objects.filter(gid=gid,sid=sid):
                    mid1.append(reports.mid1)
                    mid2.append(reports.mid2)
                    rtu.append(reports.rtu)
                    subCodelist.append(subCode)
                    subNamelist.append(subName)
          
            return Response({
                'mid1':mid1,
                'mid2':mid2,
                'rtu':rtu,
                'subCode':subCodelist,
                'subName':subNamelist
            })
        
        raise AuthenticationFailed('unauthenticated')


class AttendanceReportAPI(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            gid = user.gid
            email = user.email
            bc = email[5:7].upper()
            attendenceReport = []
            semid = user.semid
            for subjects in Semester_wise_subject.objects.filter(semid=semid,branch_code=bc):
                sid = subjects.id
                subName = subjects.subject_name
                subCode = subjects.subject_code
                
                for attendence in AttendenceReports.objects.filter(gid=gid,sid=sid):
                    attendenceReport.append({
                        'gid':gid,'subject':subName,'subCode':subCode,'current':attendence.current,'required':attendence.required
                    })
          
            return Response({
                'data':attendenceReport
            })
        
        raise AuthenticationFailed('unauthenticated')


# #event_listAPI
# @csrf_exempt
# def event_list(request):
#     if request.method=="POST":
#         eventList = []
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         data = JSONParser().parse(stream)
#         case1 = Q(branch=data['branch'])
#         case2 = Q(branch="All")
#         date1 = date.today().strftime("%Y-%m")
#         for event in Event.objects.filter(case1 | case2):
#             if event.date.strftime("%Y-%m") == date1:
#                 msg = {'title':event.title,'desc':event.desc,'event':event.event,'date':event.date}
#                 eventList.append(msg)
        
#         if len(eventList)>0:
#             msg = {'data':eventList}
#             json_data = JSONRenderer().render(msg)
#             return HttpResponse(json_data,content_type='application/json')        
#         else:
#             message = {'msg':'No Data Available'}
#             json_data = JSONRenderer().render(message)
#             return HttpResponse(json_data,content_type='application/json')
