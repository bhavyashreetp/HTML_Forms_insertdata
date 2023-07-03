from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def first(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('Data is Submitted')
    return render(request,'first.html')


def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']

        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Insertion of Topic is Done')

    return render(request,'insert_topic.html')

def insert_webpage(request):
    topic=Topic.objects.all()
    d={'topic':topic}

    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST.get('na')
        ur=request.POST['ur']

        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()
        return HttpResponse('Webpage is Created')
    
    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    webpage=Webpage.objects.all()
    d={'webpage':webpage}

    if request.method=='POST':
        n=request.POST['n']
        d=request.POST['d']
        au=request.POST['au']
        WO=Webpage.objects.get(name=n)
        WO.save()
        AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=au)[0]
        AO.save()
        return HttpResponse('data inserted to accessrecord')
        
    
    return render(request,'insert_accessrecord.html',d)




    



