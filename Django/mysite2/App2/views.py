from django.shortcuts import render
# from django.http import HttpResponse
# from App2.models import user
from App2.forms import NewUserForm

# Create your views here.
# def index(request):
#     return HttpResponse(" <em> WELCOME TO DJANGO WORLD IAM SAIKUMAR BELONGS TO ANDHRAPRADESH </em>")

# def help(request):
#     dict = {'help_insert' : " HELP PAGE! "}
#     return render(request, 'App2/help.html', context = dict)

def index(request):
    return render(request,'App2/index.html')

def users(request):
    # user_list = user.objects.order_by('first_name')
    # user_dict = { 'users': user_list}
    # return render(request,'App2/users.html',context = user_dict)
    form = NewUserForm
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print(" INVALID ERROR ")
    return render(request,'App2/users.html',{'form':form})
