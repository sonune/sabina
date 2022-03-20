from django.contrib import admin
from django.urls import path
from loveApp.views import views
from loveApp.views import contect_me
import loveApp

admin.site.site_header = "Sabina Admin Panal"
admin.site.site_title = "Sabina Admin Portal"
admin.site.index_title = 'aayatApp'

urlpatterns = [
    path('Sabina/', admin.site.urls),
    path('',views.home, name = 'home'),
    path('Days_left', views.Days_left, name = 'Days_left'),
    path('Contect_me',contect_me.Contect_me , name = 'Contect_me'),
    path('Our_Story',views.Story , name = 'Story'),
    path('Our_Future+Voices',views.Future_Voices, name = 'Story'),
    path('getout',views.Out , name = 'getout'),
    path('event',views.Event , name = 'event'),
    path('uska_massage',contect_me.uska_massage , name = 'uska_massage'),
    path('uska_question_mera_answer',contect_me.uska_question_mera_answer , name = 'uska_question_mera_answer'),
    path('mera_question_uska_answer', contect_me.mera_question_uska_answer ,name = 'mera_question_uska_answer'),
    path('Website_Manual',views.Website_Manual , name = 'Website_Manual')

    # idea = koi form agar dekhna hai ki kitna baar wo page visit kiya gaya ho to uska return wala view me redirect daal dena
]
