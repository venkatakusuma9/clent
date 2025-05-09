from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import memberForm
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

def helloworld(request):
    print("this is my first page")
    return HttpResponse("<center>Hello world")

def sayhi(request):
    print("this is my second page")
    return HttpResponse("<center>hi, how are you")

def mainpage(request):
    template=loader.get_template("mainpage.html")
    return HttpResponse(template.render())

def displayhtml(request):
    template=loader.get_template("mypage.html")
    return HttpResponse(template.render())


def displayhtml2(request):
    template=loader.get_template("mypage2.html")
    myname="kusuma"
    stuinfo={
          "name":"kusuma",
          "number":123,
          "marks":850,
          }
    context={
        "stuname":myname,
        "info":stuinfo,
        }
    return HttpResponse(template.render(context,request))

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def getAllMembers(request):
    template=loader.get_template("all_members2.html")
    mymemval = ""
    if request.method=='POST':
        mymemval =request.POST["memval"]

        print("mymem=",mymemval)
        #mymembers=Member.objects.filter(name=mymemval).values()
        mymembers=Member.objects.filter(name__contains=mymemval).values()
    else:
        mymembers=Member.objects.all().values()
        
    context={
        "allmembers":mymembers,
        "mymemval":mymemval,
        }
    return HttpResponse(template.render(context,request))

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def details(request,rid):
    template=loader.get_template("details2.html")
    mymember=Member.objects.get(id=rid)
    context={
        "mymember":mymember,
        }
    return HttpResponse(template.render(context,request))

def memberadd(request):
    if request.method=="POST":
        form=memberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("allmembers")
    else:
        form=memberForm()
        template=loader.get_template("memberAdd.html")
        context={
            "myform":form,
            }
        return HttpResponse(template.render(context,request))

def memberedit(request,rid):
    mymember=Member.objects.get(id=rid)
    if request.method=="POST":
        form=memberForm(request.POST,instance=mymember)
        if form.is_valid():
            form.save()
            return redirect("allmembers")
    else:
        form=memberForm(instance=mymember)
        template=loader.get_template("memberAdd.html")
        context={
            "myform":form,
            }
        return HttpResponse(template.render(context,request))

def memberdelete(request,rid):
    mymember=Member.objects.get(id=rid)
    mymember.delete()
    return redirect("allmembers")

