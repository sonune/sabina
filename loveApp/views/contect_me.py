from django.http import request
from django.shortcuts import redirect, render,HttpResponse
from static import mainengine
from loveApp.models.uska_question_mera_answer import Uska_Question,Mera_Jawwab
from loveApp.models.mera_question_uska_answer import Mera_sawwal,Uska_answer
from loveApp.models.uska_massage import UskaMassage
from loveApp.models.visiting_of_neha import Attendence

from django.views import View

MyQuestion = Mera_sawwal.get_My_latest_questions()
MyAnswer = Mera_Jawwab.get_Mera_latest_jawwab()
Uska_question = Uska_Question.get_Uska_latest_question()




def Contect_me(request):
    value = {
        'repeated_questions': mainengine.loveyou(),
        'MyQuestion' : MyQuestion.Mera_Specific_sawwal,
        'MyAnswer' : MyAnswer.MyAnswers,
        'UskaQuestion': Uska_question.Uska_specific_question
    }
    return render(request , 'Contect_me.html',value)

def uska_question_mera_answer(request):
    if request.method == "POST":
        uska_specific_question = request.POST.get('Uska_specific_question')
        uska_question = Uska_Question(Uska_specific_question = uska_specific_question)
        uska_question.register()
    submitted = 'Ho gaya Submit.......Thanks♥,kal check krna tabtak update ho jayga mera answer'
    value = {
        'repeated_questions': mainengine.loveyou(),
        'MyQuestion' : MyQuestion.Mera_Specific_sawwal,
        'MyAnswer' : MyAnswer.MyAnswers,
        'UskaQuestion': Uska_question.Uska_specific_question,
        'submitted' : submitted,
        'repeated_questions': mainengine.loveyou()
    }
    return render(request , 'Contect_me.html', value)

def mera_question_uska_answer(request):
    if request.method == "POST":
        Sabina_ka_Jawab_of_specifice_question = request.POST.get('Sabina_ka_Jawab_of_specifice_question')
        uska_answer = Uska_answer(Sabina_ka_Jawab_of_specifice_question = Sabina_ka_Jawab_of_specifice_question)
        uska_answer.register()
    submitted = 'Ho gaya Submit.......Thanks for your answer♥'
    value = {
            'submitted' : submitted,
            'repeated_questions': mainengine.loveyou(),
            'repeated_questions': mainengine.loveyou(),
            'MyQuestion' : MyQuestion.Mera_Specific_sawwal,
            'MyAnswer' : MyAnswer.MyAnswers,
            'UskaQuestion': Uska_question.Uska_specific_question


    }
    return render(request , 'Contect_me.html', value)

def uska_massage(request):
    if request.method == "POST":
        Repeated_questions_ka_answer = request.POST.get('repeated_questions_ka_answer')
        kaisi_ho_ka_answer = request.POST.get('kaisi_ho_ka_answer')
        Uska_massage = request.POST.get('Uska_massage')
        uska_massage = UskaMassage(repeated_questions_ka_answer = Repeated_questions_ka_answer,kaisi_ho_ka_answer = kaisi_ho_ka_answer ,Uska_massage = Uska_massage)
        uska_massage.register()
    submitted = "Ho gaya Submit.......Thanks♥"
    value = {
            'submitted' : submitted,
            'repeated_questions': mainengine.loveyou(),
            'repeated_questions': mainengine.loveyou(),
            'MyQuestion' : MyQuestion.Mera_Specific_sawwal,
            'MyAnswer' : MyAnswer.MyAnswers,
            'UskaQuestion': Uska_question.Uska_specific_question

    }
    return render(request , 'Contect_me.html', value)















