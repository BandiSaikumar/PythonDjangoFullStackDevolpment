from django.shortcuts import render
from django.http import HttpResponse
from App1.models import AccessRecord,Webpage,Topic

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('data')
    dict = {'access_records': webpages_list}
    # dict = {'insert_me': " HELLO, DJANGO WORLD! IAM SAIKUMAR BELONGS TO ANDHRAPRADESH ".upper()}
    return render(request,'App1/index.html',context = dict)
