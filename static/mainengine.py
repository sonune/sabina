#This is Main Script.....................
#Importing modules...........
import threading
from time import localtime
import gtts 
from playsound import playsound
import os
from datetime import date


#............Universal values.....................
TotalDays = 2189

now = localtime()


def Day():
    let = localtime()
    return let[-2]

def year():
    let = localtime()
    return let[0]


def month():
    let = localtime()
    return let[1]



# now = (2026,5,0,3,140,12)#For testing purposes......

#.........Start........................

# 1. Changing my year start form 1 jan to 20 may and end from 31Dec to 19May that function.......


def YearChange():

    a = Day()

    if a < 140:
        a = 224 + a
    elif a == 140:
        a = 1
        print("Happy Birthday Neha.....")
    else:
        a = a - 140

    return a


# 2. Days_Count......................(Total = 2191)

def Condition():


    if (((year() == 2021) and (month() == 6 or 7 or 8 or 9 or 10 or 11 or 12)) or ((year() == 2022)and(month() == 1 or 2 or 3 or 4 or 5 == True))):
        a =  YearChange()
        remain2Days = TotalDays - a
         

    elif (((year() == 2022) and (month() == 6 or 7 or 8 or 9 or 10 or 11 or 12)) or ((year() == 2023)and(month() == 1 or 2 or 3 or 4 or 5 )))== True:
        b =  YearChange() + 365
        remain2Days = TotalDays - b
         
    elif (((year() == 2023) and (month() == 6 or 7 or 8 or 9 or 10 or 11 or 12)) or ((year() == 2024)and(month() == 1 or 2 or 3 or 4 or 5 )))== True:
        b =  YearChange() + 730
        remain2Days = TotalDays - b
         
    elif (((year() == 2024) and (month() == 6 or 7 or 8 or 9 or 10 or 11 or 12)) or ((year() == 2025)and(month() == 1 or 2 or 3 or 4 or 5 ))) == True:
        b =  YearChange() + 1096
        remain2Days = TotalDays - b
         
    elif (((year() == 2025) and (month() == 6 or 7 or 8 or 9 or 10 or 11 or 12)) or ((year() == 2026)and(month() == 1 or 2 or 3 or 4 or 5 )))== True:
        b =  YearChange() + 1461
        remain2Days = TotalDays - b
         
    elif (((year() == 2026) and (month() == 6 or 7 or 8 or 9 or 10 or 11 or 12)) or ((year() == 2027)and(month() == 1 or 2 or 3 or 4 or 5 )))== True:
        b =  YearChange() + 1826
        remain2Days = TotalDays - b
    elif (((year() == 2027) and (month() == 6 or 7 or 8 or 9 or 10 or 11 or 12)) or ((year() == 2028)and(month() == 1 or 2 or 3 or 4 or 5 )))== True:
        b =  YearChange() + 2191
        remain2Days = TotalDays - b
    elif (((year() == 2028) and (month() == 6 or 7 or 8 or 9 or 10 or 11 or 12)) or ((year() == 2029)and(month() == 1 or 2 or 3 or 4 or 5 )))== True:
        b =  YearChange() + 2557
        remain2Days = TotalDays - b
    elif (((year() == 2029) and (month() == 6 or 7 or 8 or 9 or 10 or 11 or 12)) or ((year() == 2030)and(month() == 1 or 2 or 3 or 4 or 5 )))== True:
        b =  YearChange() + 2922
        remain2Days = TotalDays - b
    elif (((year() == 2030) and (month() == 6 or 7 or 8 or 9 or 10 or 11 or 12)) or ((year() == 2031)and(month() == 1 or 2 or 3 or 4 or 5 )))== True:
        b =  YearChange() + 3287
        remain2Days = TotalDays - b
    elif (((year() == 2031) and (month() == 6 or 7 or 8 or 9 or 10 or 11 or 12)) or ((year() == 2032)and(month() == 1 or 2 or 3 or 4 or 5 )))== True:
        b =  YearChange() + 3652
        remain2Days = TotalDays - b
    elif (((year() == 2032) and (month() == 6 or 7 or 8 or 9 or 10 or 11 or 12)) or ((year() == 2033)and(month() == 1 or 2 or 3 or 4 or 5 )))== True:
        b =  YearChange() + 4018
        remain2Days = TotalDays - b
    else:
        remain2Days = 'Done..Now your Turn'

    return remain2Days



#3. Voice Manager............

def Voice1():
    Speak = f'''हस रहा है? खुश हो रहा है?,,, मत हो अभी तुम्हारा time नहीं है, ये सब बकवास है, झूठ है, याद करो असली खुशी तेराह अगस्त को जो मिला था, भूलो मत यह क्यों आया था, वही थी reason ,वो सारे वादे जो खुद से किए थे पूरा करो, 
    सारे वादे , केवल कुछ दिन और ,और हा उसे भूलने का सोचना भी मत, जो सोचा है वो करना , वर्ना उससे अच्छा मर जाना , दूर रहो बेकार काम और बेकार लोगो से, और negative लोगो से भी'''
    tts = gtts.gTTS(Speak)
    tts.save("static/Voices/Voice1.mp3")

def Voice2():
    Speak = f"Heyy, just wait for {Condition()} Days only , don't loose hope. Just do your work with full potential and don't listen to your Silly mind ,Just remeber what you had done with her, you are responsible for her todays Circumstances. So stop regrating and do your duty. "
    tts = gtts.gTTS(Speak)
    tts.save("static/Voices/Voice2.mp3")
    # os.remove('static/Voice.mp3')
def Voice3():
    Speak = f"Heyy , don't be demotivate, just be patience, work on every promises you had made,be consistence and believe in God, Neha will definitely love you and she will be yours,be positive."
    tts = gtts.gTTS(Speak)
    tts.save("static/Voices/Voice3.mp3")

def play():
    Voice1()
    Voice2()
    Voice3()
    return "Done"

#for Date
def Current_Date():
    now = str(date.today())
    rythem  = 'year-month-day  '
    return rythem + now 

print(Current_Date())

#for I love you.........




def loveyou():
    var = now[-4]
    if var%2 == 0:
        return "I love♥ you Neha♥ aur tum?"
    elif var%11 == 0:
        return "I miss♥ you Neha♥ aur tum?"
    elif var%19 == 0:
        return "I trust♥ you Neha♥ aur tum?"
    elif var%3 == 0:
        return "I am waiting♥ for you aur tum?"
    elif var%7 == 0:
        return "I need you♥, I love you..."

    else:
        return "Will you marry me, Neha♥?"

# print(loveyou())

