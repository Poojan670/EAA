from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse,HttpResponseRedirect
from checkin.models import Entry
from checkin.forms import NameForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from datetime import datetime, timezone,date as d
from django.utils import timezone

now = timezone.now()
# Create your views here.
def contact(request):
    context = {
        'welcome_text':"Welcome To The Contact Us Page Of EAA"
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'welcome_text':" Welcome To The About Us Page Of EAA"
    }
    return render(request, 'about.html', context)

def index(request):
    return render(request, 'index.html')


def checkin(request):
    assert isinstance(request, HttpRequest)
    entryList=Entry.objects.all().filter(timeout=None)
    count=entryList.count()
    #utc_dt = datetime.now(timezone.utc)
    #date = utc_dt.astimezone()
    date=timezone.now()
    daydate=d.today()
    if request.method=="POST":
        form=NameForm(request.POST)        
        if form.is_valid():
            name,sk=form.cleaned_data['your_name'],form.cleaned_data['secret_key']
            exist=Entry.objects.filter(name=name,secretkey=sk)
            if exist.count()>0:
                return render(request,"checkin.html",
            {'entryList':entryList if count>0 else None,
            'form':NameForm(),'date':daydate,
            'status':'Already exist' })    

            entry=Entry(name=form.cleaned_data['your_name'] ,secretkey=form.cleaned_data['secret_key'],date=date,timein=date)
            entry.save()
            return HttpResponseRedirect(reverse('checkin'))
    else:
        form=NameForm()
    return render(request,"checkin.html",{'entryList':entryList if count>0 else None,'form':form,'date':daydate,'status':"" })

@csrf_exempt
def signout(request):
    assert isinstance(request, HttpRequest)
    id=request.POST.get('id')
    secret_key=request.POST.get('secretkey')
    try:
        entry=Entry.objects.get(id=id,secretkey=secret_key)
        entry.timeout=timezone.now()
        entry.save()
    except:
        return JsonResponse({'success':False})
    return JsonResponse({'success':True})





    
