from django.shortcuts import render

# Create your views here.
def index(request):
    dict = {'text':" Hello,Django World! Iam Saikumar Belongs To Andhrapradesh. ",'number':9885688180}
    return render(request,'BasicApp/index.html',dict)

def other(request):
    return render(request,'BasicApp/other.html')

def relative(request):
    return render(request,'BasicApp/relative_urls.html')
