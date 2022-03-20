from django.http import request
from django.shortcuts import render,HttpResponse
from static import mainengine
from django.views import View
from loveApp.models.visiting_of_neha import Attendence
from loveApp.models.updates import Updates
from datetime import date

# Create your views here.

def home(request):
    context = {
        'Days_left' : date.today()
    }
    if request.method == "POST":
        i_am_there_lucky = request.POST.get('I_am_there_lucky')
        attendencesave = Attendence(I_am_there_lucky = i_am_there_lucky)
        attendencesave.register()
        data = {
            'submitted' : 'Welcome Sabina..Thanks for Coming again..I love you♥'
        }
        return render(request,'home.html', data)
    return render(request,'home.html',context )

def Days_left(request):
    context ={
        'Days_left':mainengine.Condition(),
    }
    return render(request, 'Days_left.html',context)

def Website_Manual(request):
    updates = Updates.get_all_updates()
    context ={
        'Days_left':mainengine.Condition(),
        'update' : updates,
    }
    return render(request,'Website_Manual.html', context)

# def Contect_me(request):
#     context = {
#         'repeated_questions' : mainengine.loveyou()
#     }
#     if request.method == "POST":
#         heranswer = request.POST.get("heranswer")
#         uske_jawab = HerAnswer(heranswer = heranswer)
#         uske_jawab.save()
#     return render(request, "Contect_me.html" , context)



def Story(request):
    return render(request,'Under_Devlopment.html')

def Future_Voices(request):
    Voice = {
        'Voices': mainengine.play()
    }
    return render(request,'Under_Devlopment.html',Voice)

def Event(request):
    return render(request, 'Under_Devlopment.html')

def Out(request):
    return render(request,'shift.html')


# def YourAnswer(request):
#     if request.method == "POST":
#         herquestion = request.POST.get("herquestion")
#         mere_jawab = HerAnswer(herqustion = herquestion)
#         mere_jawab.save()
#     return render(request, 'Voices.html')

# def Hermassage(request):
#     if request.method == "POST":
#         love = request.POST.get("love")
#         Condition = request.POST.get("Condition")
#         massage = request.POST.get("massage")
#         hermassage = Hermassage(love = love , Condition = Condition, massage = massage)
#         hermassage.save()
#     return render(request,'Voices.html')