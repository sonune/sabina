from django.contrib import admin
from loveApp.models import mera_question_uska_answer
from loveApp.models.mera_question_uska_answer import Mera_sawwal,Uska_answer
from loveApp.models.uska_question_mera_answer import Uska_Question,Mera_Jawwab
from loveApp.models.uska_massage import UskaMassage
from loveApp.models.visiting_of_neha import Attendence
from loveApp.models.updates import Updates

# Register your models here.

admin.site.register(UskaMassage)
admin.site.register(Mera_sawwal)
admin.site.register(Uska_answer)
admin.site.register(Uska_Question)
admin.site.register(Mera_Jawwab)
admin.site.register(Attendence)
admin.site.register(Updates)