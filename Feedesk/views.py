from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.response import Response
from rest_framework.authentication import get_authorization_header
from .models import *
from rest_framework.views import APIView
from Students.authentication import decode_access_token
from .models import *
from Students.models import *

class FeeReportViewAPI(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            gid = user.gid
            feeDetail = FeeReport.objects.filter(gid=gid).first()
            return Response({
                "totalFee":feeDetail.totalFee,
                "DueTutionFee":feeDetail.DueTutionFee,
                "DueDevelopmentFee":feeDetail.DueDevelopmentFee,
                "DueOtherFee":feeDetail.DueOtherFee,
                "TotalDueFee":feeDetail.TotalDueFee,
                "FeeDetail":feeDetail.FeeDetail.url
            })

        raise AuthenticationFailed('unauthenticated')

class FeeTransactionViewAPI(APIView):
    def post(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            transactions = []
            id = decode_access_token(token) 
            user = Student.objects.filter(pk = id).first()
            gid = user.gid
            for transaction in FeeTransaction.objects.filter(gid=gid):
                transactions.append({
                    "txnId":transaction.txnId,
                    "txnAmt":transaction.txnAmt,
                    "txnReciept":transaction.txnReciept.url
                })

            return Response({
                "data":transactions
            })

        raise AuthenticationFailed('unauthenticated')