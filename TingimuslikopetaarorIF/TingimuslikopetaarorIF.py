from random import *
from math import *


#1


#try:
#    nimi=str(input("What is your name? "))
#    if nimi==str("Juku"):
#        print(f"{nimi}, siis lähme kinno!")
#        vana=int(input("Aga kui vana sa oled? "))
#        if vana>0 and vana<=6:
#            print("Okei, siis ostame tasuta pilet")
#        elif vana>6 and vana<=14:
#            print("Okei, siis ostame lastepilet pilet")
#        elif vana>14 and vana<=65:
#            print("Okei, siis ostame täispilet pilet")
#        elif vana>65 and vana<=100:
#            print("Okei, siis ostame sooduspilet pilet")
#        elif vana<1 or vana>100:
#            print("VIGA!")
#except:
#    print("TypeError")

#2
#try:
#    nimi1=input("Mis sinu nimi on? \n")
#    nimi2=input("Mis teine nimi on? \n")
#    if nimi1.isalpha()==True and nimi2.isalpha()==True:
#        print(f"{nimi1} и {nimi2}, Te olete nabre.")
#    elif nimi1.isalpha()==False or nimi2.isalpha()==False:
#        print("no")
#except:
#    print(TypeError)

#3
#try:
#    a=float(input("Какая длинна пола? "))
#    b=float(input("Какая ширина пола? "))
#    if a>0 and b>0:
#        S=a*b
#        print(f"Площаль пола равна {S}")
#        vibor=str(input("Хотите ли вы сделать ремонт? y/n \n"))
#        if vibor==str("y"):
#            cena=float(input("Какова цена за кв.м? "))
#            if cena>0:    
#                remont=cena*S
#                print(f"Цена замены пола будет состовлять {remont} eur")
#            else:
#                print("Цифра должна быть больше 0")
#        elif vibor==str("n"):
#            print("\n")
#        else:
#            print(TypeError)
#    else:
#        print("Цифра должна быть больше 0")
#except:
#    print(TypeError)

#4
#try:
#    hind=float(input("Mis hind? "))
#    if hind>=700:
#        print("Исходная цена", hind)
#        soodushind=float(hind)*0.7
#        print("Цена со скидкой в 30% будет:", round(soodushind))
#    elif hind<700 and hind>0:
#        print("Исходная цена", hind)
#        print("Скидка начинает действовать начиная с 700 евро.")
#    elif hind<=0:
#        print(f"{hind} меньше или равна 0")
#except:
#    print(TypeError)

#5

#try:
#    n=int(input("Mitu toa korteris?"))
#    for i in range(1,n+1,1):
#        t=float(input(f"{i}. Toa temperatuur: "))
#        if t>18:
#            print("Soe.")
#        else:
#            print("Külm.")

#except:
#    print("TyperError")

#Домашний вариант#

#try:
#    degrees=int(input("Temperatuur? "))
#    if degrees>18:
#        print(degriees, "Sureem kui 18")
#    elif degriees==18:
#        print("See on komfortne tubatemperatuur")
#    else:
#        print(degrees, "Enam kui 18")
#except:
#    print(TypeError)


#6#

#p=k=l=0
#kogus=randint(1,20)
#print("Kokku on",kogus,"inimest")
#for i in range(1,kogus+1,1):
#     pikkus=randint(56,256)
#     if pikkus>170:
#        print("Pikk")
#        p+=1
#     elif pikkus>155 and pikkus<=170:
#         print("Keskmine")
#         k+=1
#     else:
#         print("Lühike")
#         l+=1
#print("\n")
#print(f"Piika kasvu {p} inimest")
#print(f"Keskmise kasvu {k} inimest")
#print(f"Lühike kasvu {l} inimest")
         
#p=k=l=0
#kogus=randint(1,20)
#print("Kokku on", kogus, "inimest")
#i=0
#while i<kogus:
#    i+=1
#    pikkus=randint(56,256)
#    if pikkus>170:
#        print("Pikk")
#        p+=1
#    elif pikkus>155 and pikkus<=170:
#         print("Keskmine")
#         k+=1
#    else:
#         print("Lühike")
#         l+=1
#print("\n")
#print(f"Piika kasvu {p} inimest")
#print(f"Keskmise kasvu {k} inimest")
#print(f"Lühike kasvu {l} inimest")





#7#


#try:
#    a=float(input("Mis on su pikkus?(Sentimeetrites): "))
#    try:
#        b=int(input("Mis on sinu sugu?(mees-1 või naine-0): "))
#        if b>1:
#            print("Error")
#        else:
#            if b==1:
#                if a<=0:
#                     print("Error")
#                else:
#                     if a<170:
#                         print("Teie pikkus on madal")
#                     elif a>=170 and a<180:
#                         print("Teie pikkus on keskmine")
#                     elif a>=180:
#                         print("Teie pikkus on kõrge")
#            else:
#                if a<=0:
#                    print("Error")
#                else:
#                    if a<160:
#                        print("Teie pikkus on madal")
#                    elif a>=160 and a<170:
#                        print("Teie pikkus on keskmine")
#                    elif a>=170:
#                        print("Teie pikkus on kõrge")
#    except:
#        print("Vale Andmetüüp")
#except:
#    print("Vale Andmetüüp")

#8#


#try:
#    a=int(input("Kas soovite piima osta?(jah-1 või ei-0): "))
#    b=int(input("Kas soovite saia osta?(jah-1 või ei-0): "))
#    c=int(input("Kas soovite leiba osta?(jah-1 või ei-0): "))
#    if a==1 and b==0 and c==0:
#        piim=0.79
#        sai=0
#        leib=0
#        S=piim+sai+leib
#        print(f"Kõik ostetud asjad maksavad {S}")
#    elif a==0 and b==1 and c==0:
#        piim=0
#        sai=0.8
#        leib=0
#        P=piim+sai+leib
#        print(f"Kõik ostetud asjad maksavad {P}")
#    elif a==0 and b==0 and c==1:
#        piim=0
#        sai=0
#        leib=0.8
#        F=piim+sai+leib
#        print(f"Kõik ostetud asjad maksavad {F}")
#    elif a==1 and b==1 and c==0:
#        piim=0.79
#        sai=0.8
#        leib=0
#        L=piim+sai+leib
#        print(f"Kõik ostetud asjad maksavad {L}")
#    elif a==0 and b==1 and c==1:
#        piim=0
#        sai=0.8
#        leib=0.8
#        O=piim+sai+leib
#        print(f"Kõik ostetud asjad maksavad {O}")
#    elif a==1 and b==0 and c==1:
#        piim=0.79
#        sai=0
#        leib=0.8
#        U=piim+sai+leib
#        print(f"Kõik ostetud asjad maksavad {U}")
#    elif a==1 and b==1 and c==1:
#        piim=0.79
#        sai=0.8
#        leib=0.8
#        A=piim+sai+leib
#        print(f"Kõik ostetud asjad maksavad {A}")
#except:
#    print("Vale Andmetüüp")


#9#


#i=0
#while i==0:
#        try:
#            a=float(input("Первая сторона: "))
#            b=float(input("Вторая сторона: "))
#            if a>0 and b>0 and a==b:
#                print("Квадрат")
#                i=1
#            else:
#                print("Не квадрат")
#        except:
#            print("Введи еще раз")


#Домашний вариант#


#try:
#    a=float(input("Utle pool a "))
#    b=float(input("Utle pool b "))
#    if a==b:
#        print("See on ruut")
#    else:
#        print("See ei ole ruut")
#except:
#    print("Value Error")

#10#


#try:
#    a=float(input("1 number "))
#    b=float(input("1 number "))
#    c=input("mis märk sa oled +-/ \n ")
#    if c==("+"):
#        print(a+b)
#    elif c==("-"):
#        print(a-b)
#    elif c==(""):
#        print(a*b)
#    elif c==("/"):
#        if b==0:
#            print("Väiksem kui 0")
#        else:
#            print(a/b)
#except:
#    print("Value Error")


#11#


#now = datetime.datetime.now()
#try:
#    a=int(input("Sisesta sünniaasta. "))
#except:
#    print("Value Error")
#b=int(now.year)
#c=int(b-a)
#print(c)
#f=c%5
#if f==0:
#    print("teil on juubel")
#else:
#    print("Kui kaju")

#12#


#try:
#    a=float(input("sisesta toote hind "))
#    if a<=10:
#        print("sul on soodus 10%",a-a0.1)
#    elif a>10:
#        print("sul on soodus 20%",a-a0.2)
#except:
#    print("Value Error")

#13#


#try:
#    a=int(input("Kas sa oled mees?(jah-1 või ei-0)"))
#    if a==1:
#        b=int(input("Kui vana sa oled? "))
#        if b>=16 and b<=18:
#            print("sa sobid")
#    else:
#        print("sa oled naine sest, et sa ei sobi")
#except:
#    print("Value Error")



