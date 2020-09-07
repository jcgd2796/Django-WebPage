from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginAuth, logout as logoutAuth

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':'You have to log in in order to see this page'})
    else:
        return render(request,'englishExercises/index.html',{})

def login(request):
    usr = request.POST['user']
    pas = request.POST['password']
    user = authenticate(request,username=usr,password = pas)
    if user is not None:
        loginAuth(request,user)
        return render(request,'englishExercises/index.html',{'welcome':'Welcome, '+usr+'.'})
    else:
        return render(request,'englishExercises/login.html',{'msg':'User or password incorrect.'})

def logout(request):
    logoutAuth(request)
    return render(request,'englishExercises/login.html',{'msg':'You have logged out, See you soon!'})

def Ex1(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':'You have to log in in order to see that page'})
    else:
        return render(request,'englishExercises/Ex1.html',{'text':''})

def correctEx1(request):
    points = 0
    errors = []
    solutions = ['is','am','is','are','are','is','is','the','are','is there','No estoy aqui','Estan en el hospital?','Donde estan?','Es ese tu libro?','No se te permite entrar alli','Detras de','Macho','Viudo','Sobrina','Sobrino']
    choices = [request.POST['select1'],request.POST['select2'],request.POST['select3'],request.POST['select4'],request.POST['select5'],request.POST['select6'],request.POST['select7'],request.POST['select8'],request.POST['select9'],request.POST['select10'],request.POST['select11'],request.POST['select12'],request.POST['select13'],request.POST['select14'],request.POST['select15'],request.POST['select16'],request.POST['select17'],request.POST['select18'],request.POST['select19'],request.POST['select20']]

    for x in range (20):
        if(solutions[x] == choices[x]):
            points+=1
        else:
            errors.append(x+1)
    if (choices[7]=='<nothing>'):
        points+=1
    if (points == 20):
        text = "You've had no errors, congratulations!"
    else:
        text = "You've had errors in number(s) "+str(errors)

    return render(request,'englishExercises/Results.html',{'points':points,'c1':choices[0],'c2':choices[1],'c3':choices[2],'c4':choices[3],'c5':choices[4],'c6':choices[5],'c7':choices[6],'c8':choices[7],'c9':choices[8],'c10':choices[9],'c11':choices[10],'c12':choices[11],'c13':choices[12],'c14':choices[13],'c15':choices[14],'c16':choices[15],'c17':choices[16],'c18':choices[17],'c19':choices[18],'c20':choices[19],'s1':solutions[0],'s2':solutions[1],'s3':solutions[2],'s4':solutions[3],'s5':solutions[4],'s6':solutions[5],'s7':solutions[6],'s8':solutions[7]+' or <nothing>','s9':solutions[8],'s10':solutions[9],'s11':solutions[10],'s12':solutions[11],'s13':solutions[12],'s14':solutions[13],'s15':solutions[14],'s16':solutions[15],'s17':solutions[16],'s18':solutions[17],'s19':solutions[18],'s20':solutions[19],'errors':text})

def Ex2(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':"You have to log in in order to see that page"})
    else:
        return render(request,'englishExercises/Ex2.html',{'text':''})

def correctEx2(request):
    points = 0
    errors = []
    solutions = ['my','his','mine',"Bodgan's",'their','on','with','in','in','between','This is a piece of the clock','No es hermoso ni feo','Esta es tu historia','Las zarpas del tigre son blancas','Es este tu telefono?','Amabilidad','Orgullo','Hija','Pariente','Mantel']
    choices = [request.POST['select1'],request.POST['select2'],request.POST['select3'],request.POST['select4'],request.POST['select5'],request.POST['select6'],request.POST['select7'],request.POST['select8'],request.POST['select9'],request.POST['select10'],request.POST['select11'],request.POST['select12'],request.POST['select13'],request.POST['select14'],request.POST['select15'],request.POST['select16'],request.POST['select17'],request.POST['select18'],request.POST['select19'],request.POST['select20']]

    for x in range (20):
        if(solutions[x] == choices[x]):
            points+=1
        else:
            errors.append(x+1)
    if (points == 20):
        text = "You've had no errors, congratulations!"
    else:
        text = "You've had errors in number(s) "+str(errors)

    return render(request,'englishExercises/Results2.html',{'points':points,'c1':choices[0],'c2':choices[1],'c3':choices[2],'c4':choices[3],'c5':choices[4],'c6':choices[5],'c7':choices[6],'c8':choices[7],'c9':choices[8],'c10':choices[9],'c11':choices[10],'c12':choices[11],'c13':choices[12],'c14':choices[13],'c15':choices[14],'c16':choices[15],'c17':choices[16],'c18':choices[17],'c19':choices[18],'c20':choices[19],'s1':solutions[0],'s2':solutions[1],'s3':solutions[2],'s4':solutions[3],'s5':solutions[4],'s6':solutions[5],'s7':solutions[6],'s8':solutions[7],'s9':solutions[8],'s10':solutions[9],'s11':solutions[10],'s12':solutions[11],'s13':solutions[12],'s14':solutions[13],'s15':solutions[14],'s16':solutions[15],'s17':solutions[16],'s18':solutions[17],'s19':solutions[18],'s20':solutions[19],'errors':text})

def Ex3(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':"You have to log in in order to see that page"})
    else:
        return render(request,'englishExercises/Ex3.html',{'text':''})

def correctEx3(request):
    points = 0
    errors = []
    solutions = ['07:40','02:05','12:00',"09:45",'00:00','have','has','walked','was','going to','will','leaves','Have to',"mustn't",'going to','Cejas','Joya','Cuchilla','Seda','Panuelo']
    choices = [request.POST['select1'],request.POST['select2'],request.POST['select3'],request.POST['select4'],request.POST['select5'],request.POST['select6'],request.POST['select7'],request.POST['select8'],request.POST['select9'],request.POST['select10'],request.POST['select11'],request.POST['select12'],request.POST['select13'],request.POST['select14'],request.POST['select15'],request.POST['select16'],request.POST['select17'],request.POST['select18'],request.POST['select19'],request.POST['select20']]

    for x in range (20):
        if(solutions[x] == choices[x]):
            points+=1
        else:
            errors.append(x+1)
    if (points == 20):
        text = "You've had no errors, congratulations!"
    else:
        text = "You've had errors in number(s) "+str(errors)

    return render(request,'englishExercises/Results3.html',{'points':points,'c1':choices[0],'c2':choices[1],'c3':choices[2],'c4':choices[3],'c5':choices[4],'c6':choices[5],'c7':choices[6],'c8':choices[7],'c9':choices[8],'c10':choices[9],'c11':choices[10],'c12':choices[11],'c13':choices[12],'c14':choices[13],'c15':choices[14],'c16':choices[15],'c17':choices[16],'c18':choices[17],'c19':choices[18],'c20':choices[19],'s1':solutions[0],'s2':solutions[1],'s3':solutions[2],'s4':solutions[3],'s5':solutions[4],'s6':solutions[5],'s7':solutions[6],'s8':solutions[7],'s9':solutions[8],'s10':solutions[9],'s11':solutions[10],'s12':solutions[11],'s13':solutions[12],'s14':solutions[13],'s15':solutions[14],'s16':solutions[15],'s17':solutions[16],'s18':solutions[17],'s19':solutions[18],'s20':solutions[19],'errors':text})

def Ex4(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':"You have to log in in order to see that page"})
    else:
        return render(request,'englishExercises/Ex4.html',{'text':''})

def correctEx4(request):
    points = 0
    errors = []
    solutions = ['will',"won't",'am',"have",'have',"The fan wasn't unplugged by me.","He's said to be rich.",'The car was taken by her.','Was I allowed by him to dye my hair?',"The train'll be taken by me tomorrow.",'Taking care of my friend, I helped him.','I saw him running away.','Having finished his homework, he played GTA V.',"While you were out, I painted this room.",'Having spoken to her boss, she went home.','Servilleta','Telon','Valer la pena','Actor','Entre ellos']
    choices = [request.POST['select1'],request.POST['select2'],request.POST['select3'],request.POST['select4'],request.POST['select5'],request.POST['select6'],request.POST['select7'],request.POST['select8'],request.POST['select9'],request.POST['select10'],request.POST['select11'],request.POST['select12'],request.POST['select13'],request.POST['select14'],request.POST['select15'],request.POST['select16'],request.POST['select17'],request.POST['select18'],request.POST['select19'],request.POST['select20']]

    for x in range (20): 
        if(solutions[x] == choices[x]):
            points+=1
        else:
            errors.append(x+1)
    if (points == 20):
        text = "You've had no errors, congratulations!"
    else:
        text = "You've had errors in number(s) "+str(errors)

    return render(request,'englishExercises/Results4.html',{'points':points,'c1':choices[0],'c2':choices[1],'c3':choices[2],'c4':choices[3],'c5':choices[4],'c6':choices[5],'c7':choices[6],'c8':choices[7],'c9':choices[8],'c10':choices[9],'c11':choices[10],'c12':choices[11],'c13':choices[12],'c14':choices[13],'c15':choices[14],'c16':choices[15],'c17':choices[16],'c18':choices[17],'c19':choices[18],'c20':choices[19],'s1':solutions[0],'s2':solutions[1],'s3':solutions[2],'s4':solutions[3],'s5':solutions[4],'s6':solutions[5],'s7':solutions[6],'s8':solutions[7],'s9':solutions[8],'s10':solutions[9],'s11':solutions[10],'s12':solutions[11],'s13':solutions[12],'s14':solutions[13],'s15':solutions[14],'s16':solutions[15],'s17':solutions[16],'s18':solutions[17],'s19':solutions[18],'s20':solutions[19],'errors':text})

def Ex5(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':"You have to log in in order to see that page"})
    else:
        return render(request,'englishExercises/Ex5.html',{'text':''})

def correctEx5(request):
    points = 0
    errors = []
    solutions = ['Coming',"Snowed",'Could',"Told",'Forgot',"Spill","Done",'Forgiven','Blew',"Become",'taller','most clever','as old as',"most terrible",'not so rich','Atestado','Corriente','Lata','Ultramar','Crudo']
    choices = [request.POST['select1'],request.POST['select2'],request.POST['select3'],request.POST['select4'],request.POST['select5'],request.POST['select6'],request.POST['select7'],request.POST['select8'],request.POST['select9'],request.POST['select10'],request.POST['select11'],request.POST['select12'],request.POST['select13'],request.POST['select14'],request.POST['select15'],request.POST['select16'],request.POST['select17'],request.POST['select18'],request.POST['select19'],request.POST['select20']]

    for x in range (20):
        if(solutions[x] == choices[x]):
            points+=1
        else:
            errors.append(x+1)
    if (points == 20):
        text = "You've had no errors, congratulations!"
    else:
        text = "You've had errors in number(s) "+str(errors)

    return render(request,'englishExercises/Results5.html',{'points':points,'c1':choices[0],'c2':choices[1],'c3':choices[2],'c4':choices[3],'c5':choices[4],'c6':choices[5],'c7':choices[6],'c8':choices[7],'c9':choices[8],'c10':choices[9],'c11':choices[10],'c12':choices[11],'c13':choices[12],'c14':choices[13],'c15':choices[14],'c16':choices[15],'c17':choices[16],'c18':choices[17],'c19':choices[18],'c20':choices[19],'s1':solutions[0],'s2':solutions[1],'s3':solutions[2],'s4':solutions[3],'s5':solutions[4],'s6':solutions[5],'s7':solutions[6],'s8':solutions[7],'s9':solutions[8],'s10':solutions[9],'s11':solutions[10],'s12':solutions[11],'s13':solutions[12],'s14':solutions[13],'s15':solutions[14],'s16':solutions[15],'s17':solutions[16],'s18':solutions[17],'s19':solutions[18],'s20':solutions[19],'errors':text})

def Ex6(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':"You have to log in in order to see that page"})
    else:
        return render(request,'englishExercises/Ex6.html',{'text':''})

def correctEx6(request):
    points = 0
    errors = []
    solutions = ['might',"mustn't",'should',"must","mustn't","Diana has forgotten her homework.","I don't want to come because I have already seen that film.",'.','Alex has lost his watch.',"Pedro hadn't been bungee jumping before.",'Have you eaten anything since yesterday?','Please can we stop and rest? we have been walking for hours.','Eric is very excited, he had never visited Cyprus before.',"Have you seen Tom Cruise's new film yet?","Where's the watch I lent you, what have you done with it?",'Your face is red, what have you done?','Miguel, who is very tall, is good at basketball.','Lionel Messi is the footballer who scored the most goals in La Liga last year.','Rafael Nadal, who comes from Majorca, has won thirteen Grand Slam titles.','The Thames is the river in London where the famous Oxford vs Cambridge boat race is held.','This is the tennis racket with which I won the final.']
    choices = [request.POST['select1'],request.POST['select2'],request.POST['select3'],request.POST['select4'],request.POST['select5'],request.POST['select6'],request.POST['select7'],request.POST['select8'],request.POST['select9'],request.POST['select10'],request.POST['select11'],request.POST['select12'],request.POST['select13'],request.POST['select14'],request.POST['select15'],request.POST['select16'],request.POST['select17'],request.POST['select18'],request.POST['select19'],request.POST['select20'],request.POST['select21']]

    for x in range (21):
        if(solutions[x] == choices[x]):
            points+=1
        else:
            errors.append(x+1)
    if (points == 21):
        text = "You've had no errors, congratulations!"
    else:
        text = "You've had errors in number(s) "+str(errors)

    return render(request,'englishExercises/Results6.html',{'points':points,'c1':choices[0],'c2':choices[1],'c3':choices[2],'c4':choices[3],'c5':choices[4],'c6':choices[5],'c7':choices[6],'c8':choices[7],'c9':choices[8],'c10':choices[9],'c11':choices[10],'c12':choices[11],'c13':choices[12],'c14':choices[13],'c15':choices[14],'c16':choices[15],'c17':choices[16],'c18':choices[17],'c19':choices[18],'c20':choices[19],'c21':choices[20],'s1':solutions[0],'s2':solutions[1],'s3':solutions[2],'s4':solutions[3],'s5':solutions[4],'s6':solutions[5],'s7':solutions[6],'s8':solutions[7],'s9':solutions[8],'s10':solutions[9],'s11':solutions[10],'s12':solutions[11],'s13':solutions[12],'s14':solutions[13],'s15':solutions[14],'s16':solutions[15],'s17':solutions[16],'s18':solutions[17],'s19':solutions[18],'s20':solutions[19],'s21':solutions[20],'errors':text})

def Ex7(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':"You have to log in in order to see that page"})
    else:
        return render(request,'englishExercises/Ex7.html',{'text':''})

def correctEx7(request):
    points = 0
    errors = []
    solutions = ['The shoplifter was arrested this morning.',"Discounts will be offered by shoppers next week.",'The ring was stolen from the jewellers last week.',"Will the new shopping centre be opened by the major tomorrow?","Will this shirt be worn by David Beckham next season?","that","(who)",'what','that',"what",'that','Lucy said that she has spoken to her friend on Skype the day before.',"Max told me he would take a photo of me.","Maria's mother told me to tell her if I changed my email adress. ",'Dad told Peter he had been online for too long.',"They said they had never used that website before.",'Stephanie said she was going to look that up on the Internet then to find out more.','They had a photo taken yesterday.','I had my leg bitten by a dog.','Theo always gets his hair cut by the same hairdresser.','.','The shoppers had their bags packed.']
    choices = [request.POST['select1'],request.POST['select2'],request.POST['select3'],request.POST['select4'],request.POST['select5'],request.POST['select6'],request.POST['select7'],request.POST['select8'],request.POST['select9'],request.POST['select10'],request.POST['select11'],request.POST['select12'],request.POST['select13'],request.POST['select14'],request.POST['select15'],request.POST['select16'],request.POST['select17'],request.POST['select18'],request.POST['select19'],request.POST['select20'],request.POST['select21'],request.POST['select22']]

    for x in range (22):
        if(solutions[x] == choices[x]):
            points+=1
        else:
            errors.append(x+1)
    if (points == 21):
        text = "You've had no errors, congratulations!"
    else:
        text = "You've had errors in number(s) "+str(errors)

    return render(request,'englishExercises/Results7.html',{'points':points,'c1':choices[0],'c2':choices[1],'c3':choices[2],'c4':choices[3],'c5':choices[4],'c6':choices[5],'c7':choices[6],'c8':choices[7],'c9':choices[8],'c10':choices[9],'c11':choices[10],'c12':choices[11],'c13':choices[12],'c14':choices[13],'c15':choices[14],'c16':choices[15],'c17':choices[16],'c18':choices[17],'c19':choices[18],'c20':choices[19],'c21':choices[20],'c22':choices[21],'s1':solutions[0],'s2':solutions[1],'s3':solutions[2],'s4':solutions[3],'s5':solutions[4],'s6':solutions[5],'s7':solutions[6],'s8':solutions[7],'s9':solutions[8],'s10':solutions[9],'s11':solutions[10],'s12':solutions[11],'s13':solutions[12],'s14':solutions[13],'s15':solutions[14],'s16':solutions[15],'s17':solutions[16],'s18':solutions[17],'s19':solutions[18],'s20':solutions[19],'s21':solutions[20],'s22':solutions[21],'errors':text})

def Ex8(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':"You have to log in in order to see that page"})
    else:
        return render(request,'englishExercises/Ex8.html',{'text':''})

def correctEx8(request):
    points = 0
    errors = []
    solutions = ['will be playing',"will have gone",'will have spent',"will have worked","will be cycling","was given","was passed",'was sent','was brought',"was taught",'were told','My aunt said that she would check her messages before we left.',"Tom said that he was going to the cinema that night.",".",'Michael said that he had seen my brother the day before.']
    choices = [request.POST['select1'],request.POST['select2'],request.POST['select3'],request.POST['select4'],request.POST['select5'],request.POST['select6'],request.POST['select7'],request.POST['select8'],request.POST['select9'],request.POST['select10'],request.POST['select11'],request.POST['select12'],request.POST['select13'],request.POST['select14'],request.POST['select15']]

    for x in range (15):
        if(solutions[x] == choices[x]):
            points+=1
        else:
            errors.append(x+1)
    if (points == 15):
        text = "You've had no errors, congratulations!"
    else:
        text = "You've had errors in number(s) "+str(errors)

    return render(request,'englishExercises/Results8.html',{'points':points,'c1':choices[0],'c2':choices[1],'c3':choices[2],'c4':choices[3],'c5':choices[4],'c6':choices[5],'c7':choices[6],'c8':choices[7],'c9':choices[8],'c10':choices[9],'c11':choices[10],'c12':choices[11],'c13':choices[12],'c14':choices[13],'c15':choices[14],'s1':solutions[0],'s2':solutions[1],'s3':solutions[2],'s4':solutions[3],'s5':solutions[4],'s6':solutions[5],'s7':solutions[6],'s8':solutions[7],'s9':solutions[8],'s10':solutions[9],'s11':solutions[10],'s12':solutions[11],'s13':solutions[12],'s14':solutions[13],'s15':solutions[14],'errors':text})

def Voc1(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':'You have to log in in order to see this page'})
    else:
        return render(request,'englishExercises/Vocabulary1.html',{})

def Voc2(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':'You have to log in in order to see this page'})
    else:
        return render(request,'englishExercises/Vocabulary2.html',{})

def Voc3(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':'You have to log in in order to see this page'})
    else:
        return render(request,'englishExercises/Vocabulary3.html',{})

def Voc4(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':'You have to log in in order to see this page'})
    else:
        return render(request,'englishExercises/Vocabulary4.html',{})

def Voc5(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':'You have to log in in order to see this page'})
    else:
        return render(request,'englishExercises/Vocabulary5.html',{})

    
def Verbs1(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':'You have to log in in order to see this page'})
    else:
        return render(request,'englishExercises/Verbs1.html',{})

def Verbs2(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':'You have to log in in order to see this page'})
    else:
        return render(request,'englishExercises/Verbs2.html',{})

def Verbs3(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':'You have to log in in order to see this page'})
    else:
        return render(request,'englishExercises/Verbs3.html',{})

def Verbs4(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':'You have to log in in order to see this page'})
    else:
        return render(request,'englishExercises/Verbs4.html',{})

def About(request):
    if not request.user.is_authenticated:
        return render(request,'englishExercises/login.html',{'msg':'You have to log in in order to see this page'})
    else:
        return render(request,'englishExercises/about.html',{})
