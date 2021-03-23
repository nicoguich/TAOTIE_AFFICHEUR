import board
import time
import string
import random
from adafruit_ht16k33.segments import Seg14x4


ism = open("ism.txt", "r")
num_lines_ism = sum(1 for line in open('ism.txt'))

prob_ism=[None]*num_lines_ism
list_ism=[None]*num_lines_ism
lettre_ism=[None]*15


pre = open("pre.txt", "r")
num_lines_pre= sum(1 for line in open('pre.txt'))

prob_pre=[None]*num_lines_pre
list_pre=[None]*num_lines_pre
lettre_pre=[None]*8






print ("________________ISM______________________")

index_ism=0
for line in ism:
    list_ism[index_ism]=line
    list_ism[index_ism]=list_ism[index_ism][:-1]
    list_ism[index_ism]=list_ism[index_ism].upper()
    print(list_ism[index_ism])
    split_ism=list_ism[index_ism].split("/")
    list_ism[index_ism]=split_ism[0]
    try:
        prob_ism[index_ism]=split_ism[1]
    except :
        prob_ism[index_ism]=0
        pass



    index_ism+=1


print()
print ("________________PRE______________________")

index_pre=0
for line in pre:
    list_pre[index_pre]=line
    list_pre[index_pre]=list_pre[index_pre][:-1]
    list_pre[index_pre]=list_pre[index_pre].upper()
    print(list_pre[index_pre])
    split_pre=list_pre[index_pre].split("/")
    list_pre[index_pre]=split_pre[0]
    try:
        prob_pre[index_pre]=split_pre[1]
    except :
        prob_pre[index_pre]=0
        pass



    index_pre+=1




i2c = board.I2C()
display1 = Seg14x4(i2c, address=0x70)
display2 = Seg14x4(i2c, address=0x71)
display3 = Seg14x4(i2c, address=0x72)
display4 = Seg14x4(i2c, address=0x73)
display5 = Seg14x4(i2c, address=0x74)
display6 = Seg14x4(i2c, address=0x75)

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


while True :

    random_ism=random.randint(0, num_lines_ism-1)
    random_pre=random.randint(0, num_lines_pre-1)

    ism_choisi= list_ism[random_ism]
    pre_choisi=list_pre[random_pre]
    print(pre_choisi)



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

    display1.print(''.join(mot1_list))
    display2.print(''.join(mot2_list))
    display3.print(''.join(mot3_list))
    display4.print(''.join(mot4_list))
    display5.print(''.join(mot5_list))
    display6.print(''.join(mot6_list))
    time.sleep(3)
