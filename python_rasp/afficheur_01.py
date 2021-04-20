import RPi.GPIO as GPIO
import board
import time
import string
import random
from adafruit_ht16k33.segments import Seg14x4
from convert_binaire import convert_bin




adresse=0


GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)




display1_connect= False
display2_connect= False
display3_connect= False
display4_connect= False
display5_connect= False
display6_connect= False



i2c = board.I2C()

try :
    display1 = Seg14x4(i2c, address=0x70)
    display1_connect= True
except:
    pass
try:
    display2 = Seg14x4(i2c, address=0x71)
    display2_connect= True
except:
    pass
try:
    display3 = Seg14x4(i2c, address=0x72)
    display3_connect= True
except:
    pass
try:
    display4 = Seg14x4(i2c, address=0x73)
    display4_connect= True
except:
    pass
try:
    display5 = Seg14x4(i2c, address=0x74)
    display5_connect= True
except:
    pass
try:
    display6 = Seg14x4(i2c, address=0x75)
    display6_connect= True
except:
    pass

str_temp = ""
pre_bin_in = [0,0,0,0,0,0,0,0]
pre_bin_out = [0,0,0,0,0,0,0,0]
ism_bin_in = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ism_bin_out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]




ism = open("ism.txt", "r")
num_lines_ism = sum(1 for line in open('ism.txt'))
prob_ism=[None]*num_lines_ism
list_ism=[None]*num_lines_ism
lettre_ism=[None]*15
index_ism=0
for line in ism:
    list_ism[index_ism]=line
    list_ism[index_ism]=list_ism[index_ism][:-1]
    list_ism[index_ism]=list_ism[index_ism].upper()
    split_ism=list_ism[index_ism].split("/")
    list_ism[index_ism]=split_ism[0]
    try:
        prob_ism[index_ism]=split_ism[1]
    except :
        prob_ism[index_ism]=0
        pass
    index_ism+=1







pre = open("pre.txt", "r")
num_lines_pre= sum(1 for line in open('pre.txt'))
prob_pre=[None]*num_lines_pre
list_pre=[None]*num_lines_pre
lettre_pre=[None]*8
index_pre=0
for line in pre:
    list_pre[index_pre]=line
    list_pre[index_pre]=list_pre[index_pre][:-1]
    list_pre[index_pre]=list_pre[index_pre].upper()
    split_pre=list_pre[index_pre].split("/")
    list_pre[index_pre]=split_pre[0]
    try:
        prob_pre[index_pre]=split_pre[1]
    except :
        prob_pre[index_pre]=0
        pass
    index_pre+=1





mot1= "    "
mot2= "    "
mot3= "    "
mot4= "    "
mot5= "    "
mot6= "    "
mot1_list = list(mot1)
mot2_list = list(mot2)
mot3_list = list(mot3)
mot4_list = list(mot4)
mot5_list = list(mot5)
mot6_list = list(mot6)



segment =[None]*24
for i in range(0,24):

    segment[i]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]





def morph(lettre_in,lettre_out,compteur,compteur_lettre):

    global segment

    random_segment=random.randint(0, 17)
    if segment[compteur_lettre][random_segment]==1:
        while segment[compteur_lettre][random_segment]==1:
            random_segment=random.randint(0, 17)
    segment[compteur_lettre][random_segment]=1


    CHAR_IN=list(lettre_in)
    CHAR_OUT=list(lettre_out)

    str1 = ""
    str2 = ""
    if CHAR_IN[random_segment]!=CHAR_OUT[random_segment]:
        if CHAR_IN[random_segment]=='0':
            CHAR_IN[random_segment]='1'
            return CHAR_IN



        elif CHAR_IN[random_segment]=='1':
            CHAR_IN[random_segment]='0'

            return CHAR_IN

    else :

        return CHAR_IN




while True :

    if display1_connect==False:
        try :
            display1 = Seg14x4(i2c, address=0x70)
            display1_connect= True
        except:
            display1_connect= False
            pass
    if display2_connect==False:
        try:
            display2 = Seg14x4(i2c, address=0x71)
            display2_connect= True
        except:
            display2_connect= False
            pass
    if display3_connect==False:
        try:
            display3 = Seg14x4(i2c, address=0x72)
            display3_connect= True
        except:
            display3_connect= False
            pass
    if display4_connect==False:
        try:
            display4 = Seg14x4(i2c, address=0x73)
            display4_connect= True
        except:
            display4_connect= False
            pass
    if display5_connect==False:
        try:
            display5 = Seg14x4(i2c, address=0x74)
            display5_connect= True
        except:
            display5_connect= False
            pass
    if display6_connect==False:
        try:
            display6 = Seg14x4(i2c, address=0x75)
            display6_connect= True
        except:
            display6_connect= False
            pass





    adresse=0
    if GPIO.input(23):
        adresse=adresse+2**6
    if GPIO.input(24):
        adresse=adresse+2**5
    if GPIO.input(25):
        adresse=adresse+2**4
    if GPIO.input(7):
        adresse=adresse+2**3
    if GPIO.input(12):
        adresse=adresse+2**2
    if GPIO.input(16):
        adresse=adresse+2**1
    if GPIO.input(20):
        adresse=adresse+2**0
    if GPIO.input(21):
        test= True
    else:
        test=False
    print("adresse: "+str(adresse))




    if test==False:



        random_ism=random.randint(0, num_lines_ism-1)
        random_pre=random.randint(0, num_lines_pre-1)

        ism_choisi= list_ism[random_ism]
        pre_choisi=list_pre[random_pre]
        print(pre_choisi+"_"+ism_choisi)



        for x in range(8) :
            lettre_pre[x]=' '

        for x in range(8-len(pre_choisi),8):
            lettre_pre[x]=pre_choisi[x-(8-len(pre_choisi))]



        for x in range(15) :
            try :
                lettre_ism[x]=ism_choisi[x]
            except:
                lettre_ism[x]=' '
                pass


        for x in range (8):

            pre_bin_out[x]=convert_bin(lettre_pre[x])
            if x<=3 :
                pre_bin_in[x]=convert_bin(mot1_list[x])
            else :
                pre_bin_in[x]=convert_bin(mot2_list[x-4])








        for x in range (15):

            ism_bin_out[x]=convert_bin(lettre_ism[x])
            if x<=2 :
                ism_bin_in[x]=convert_bin(mot3_list[x+1])
            elif x>2 and x<=6 :
                ism_bin_in[x]=convert_bin(mot4_list[x-3])
            elif x>6 and x<=10 :
                ism_bin_in[x]=convert_bin(mot5_list[x-7])
            elif x>10 :
                ism_bin_in[x]=convert_bin(mot6_list[x-11])



        for i in range(0,24):
            segment[i]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


        for x in range(0,18):
            for y in range (8):
                pre_bin_in[y]=morph(pre_bin_in[y],pre_bin_out[y],x,y)
            for y in range (15):
                ism_bin_in[y]=morph(ism_bin_in[y],ism_bin_out[y],x,y+8)


            s=''
            if display1_connect:
                try:
                    display1.set_digit_raw(0,int(s.join(pre_bin_in[0]),2))
                    display1.set_digit_raw(1,int(s.join(pre_bin_in[1]),2))
                    display1.set_digit_raw(2,int(s.join(pre_bin_in[2]),2))
                    display1.set_digit_raw(3,int(s.join(pre_bin_in[3]),2))
                except:
                    display1_connect=False
                    pass
            if display2_connect:
                try:
                    display2.set_digit_raw(0,int(s.join(pre_bin_in[4]),2))
                    display2.set_digit_raw(1,int(s.join(pre_bin_in[5]),2))
                    display2.set_digit_raw(2,int(s.join(pre_bin_in[6]),2))
                    display2.set_digit_raw(3,int(s.join(pre_bin_in[7]),2))
                except:
                    display2_connect=False
                    pass
            if display3_connect:
                try:
                    display3.set_digit_raw(1,int(s.join(ism_bin_in[0]),2))
                    display3.set_digit_raw(2,int(s.join(ism_bin_in[1]),2))
                    display3.set_digit_raw(3,int(s.join(ism_bin_in[2]),2))
                except:
                    display3_connect=False
                    pass
            if display4_connect:
                try:
                    display4.set_digit_raw(0,int(s.join(ism_bin_in[3]),2))
                    display4.set_digit_raw(1,int(s.join(ism_bin_in[4]),2))
                    display4.set_digit_raw(2,int(s.join(ism_bin_in[5]),2))
                    display4.set_digit_raw(3,int(s.join(ism_bin_in[6]),2))
                except:
                    display4_connect=False
                    pass
            if display5_connect:
                try:
                    display5.set_digit_raw(0,int(s.join(ism_bin_in[7]),2))
                    display5.set_digit_raw(1,int(s.join(ism_bin_in[8]),2))
                    display5.set_digit_raw(2,int(s.join(ism_bin_in[9]),2))
                    display5.set_digit_raw(3,int(s.join(ism_bin_in[10]),2))
                except:
                    display5_connect=False
                    pass
            if display6_connect:
                try:
                    display6.set_digit_raw(0,int(s.join(ism_bin_in[11]),2))
                    display6.set_digit_raw(1,int(s.join(ism_bin_in[12]),2))
                    display6.set_digit_raw(2,int(s.join(ism_bin_in[13]),2))
                    display6.set_digit_raw(3,int(s.join(ism_bin_in[14]),2))
                except:
                    display6_connect=False
                    pass
            time.sleep(0.5)









        mot1_list[0]=lettre_pre[0]
        mot1_list[1]=lettre_pre[1]
        mot1_list[2]=lettre_pre[2]
        mot1_list[3]=lettre_pre[3]

        mot2_list[0]=lettre_pre[4]
        mot2_list[1]=lettre_pre[5]
        mot2_list[2]=lettre_pre[6]
        mot2_list[3]=lettre_pre[7]

        mot3_list[0]="_"
        mot3_list[1]=lettre_ism[0]
        mot3_list[2]=lettre_ism[1]
        mot3_list[3]=lettre_ism[2]

        mot4_list[0]=lettre_ism[3]
        mot4_list[1]=lettre_ism[4]
        mot4_list[2]=lettre_ism[5]
        mot4_list[3]=lettre_ism[6]

        mot5_list[0]=lettre_ism[7]
        mot5_list[1]=lettre_ism[8]
        mot5_list[2]=lettre_ism[9]
        mot5_list[3]=lettre_ism[10]

        mot6_list[0]=lettre_ism[11]
        mot6_list[1]=lettre_ism[12]
        mot6_list[2]=lettre_ism[13]
        mot6_list[3]=lettre_ism[14]
        if display1_connect:
            try:
                display1.print(''.join(mot1_list))
            except:
                display1_connect=False
                pass
        if display2_connect:
            try:
                display2.print(''.join(mot2_list))
            except:
                display2_connect=False
                pass
        if display3_connect:
            try:
                display3.print(''.join(mot3_list))
            except:
                display3_connect=False
                pass
        if display4_connect:
            try:
                display4.print(''.join(mot4_list))
            except:
                display4_connect=False
                pass
        if display5_connect:
            try:
                display5.print(''.join(mot5_list))
            except:
                display5_connect=False
                pass
        if display6_connect:
            try:
                display6.print(''.join(mot6_list))
            except:
                display6_connect=False
                pass
        time.sleep(3)

    else :

        if display1_connect:
            try:
                display1.set_digit_raw(0,int("0b0011111111111111",2))
                display1.set_digit_raw(1,int("0b0011111111111111",2))
                display1.set_digit_raw(2,int("0b0011111111111111",2))
                display1.set_digit_raw(3,int("0b0011111111111111",2))
            except:
                display1_connect=False
                pass
        if display2_connect:
            try:
                display2.set_digit_raw(0,int("0b0011111111111111",2))
                display2.set_digit_raw(1,int("0b0011111111111111",2))
                display2.set_digit_raw(2,int("0b0011111111111111",2))
                display2.set_digit_raw(3,int("0b0011111111111111",2))
            except:
                display2_connect=False
                pass
        if display3_connect:
            try:
                display3.set_digit_raw(0,int("0b0011111111111111",2))
                display3.set_digit_raw(1,int("0b0011111111111111",2))
                display3.set_digit_raw(2,int("0b0011111111111111",2))
                display3.set_digit_raw(3,int("0b0011111111111111",2))
            except:
                display3_connect=False
                pass
        if display4_connect:
            try:
                display4.set_digit_raw(0,int("0b0011111111111111",2))
                display4.set_digit_raw(1,int("0b0011111111111111",2))
                display4.set_digit_raw(2,int("0b0011111111111111",2))
                display4.set_digit_raw(3,int("0b0011111111111111",2))
            except:
                display4_connect=False
                pass
        if display5_connect:
            try:
                display5.set_digit_raw(0,int("0b0011111111111111",2))
                display5.set_digit_raw(1,int("0b0011111111111111",2))
                display5.set_digit_raw(2,int("0b0011111111111111",2))
                display5.set_digit_raw(3,int("0b0011111111111111",2))
            except:
                display5_connect=False
                pass
        if display6_connect:
            try:
                display6.set_digit_raw(0,int("0b0011111111111111",2))
                display6.set_digit_raw(1,int("0b0011111111111111",2))
                display6.set_digit_raw(2,int("0b0011111111111111",2))
                display6.set_digit_raw(3,int("0b0011111111111111",2))
            except:
                display6_connect=False
                pass
        time.sleep(3)
        if display1_connect:
            try:
                display1.print("1111")
            except:
                display1_connect=False
                pass
        if display2_connect:
            try:
                display2.print("2222")
            except:
                display2_connect=False
                pass
        if display3_connect:
            try:
                display3.print("3333")
            except:
                display3_connect=False
                pass
        if display4_connect:
            try:
                display4.print("4444")
            except:
                display4_connect=False
                pass
        if display5_connect:
            try:
                display5.print("5555")
            except:
                display5_connect=False
                pass
        if display6_connect:
            try:
                display6.print("6666")
            except:
                display6_connect=False
                pass
        time.sleep(3)
