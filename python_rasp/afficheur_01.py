import board
import time
import string
import random
from adafruit_ht16k33.segments import Seg14x4


test= True

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
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
CHARS = ["0b0000000000000000", #
"0b0100000000000110", # !
"0b0000001000100000", # "
"0b0001001011001110", # #
"0b0001001011101101", # $
"0b0000110000100100", # %
"0b0010001101011101", # &
"0b0000010000000000", # '
"0b0010010000000000", # (
"0b0000100100000000", # )
"0b0011111111000000", # *
"0b0001001011000000", # +
"0b0000100000000000", # ,
"0b0000000011000000", # -
"0b0000000000000000", # .
"0b0000110000000000", # /
"0b0000110000111111", # 0
"0b0000000000000110", # 1
"0b0000000011011011", # 2
"0b0000000010001111", # 3
"0b0000000011100110", # 4
"0b0010000001101001", # 5
"0b0000000011111101", # 6
"0b0000000000000111", # 7
"0b0000000011111111", # 8
"0b0000000011101111", # 9
"0b0001001000000000", # :
"0b0000101000000000", # ;
"0b0010010001000000", # <
"0b0000000011001000", # =
"0b0000100110000000", # >
"0b0110000010100011", # ?
"0b0000001010111011", # @
"0b0000000011110111", # A
"0b0001001010001111", # B
"0b0000000000111001", # C
"0b0001001000001111", # D
"0b0000000011111001", # E
"0b0000000001110001", # F
"0b0000000010111101", # G
"0b0000000011110110", # H
"0b0001001000000000", # I
"0b0000000000011110", # J
"0b0010010001110000", # K
"0b0000000000111000", # L
"0b0000010100110110", # M
"0b0010000100110110", # N
"0b0000000000111111", # O
"0b0000000011110011", # P
"0b0010000000111111", # Q
"0b0010000011110011", # R
"0b0000000011101101", # S
"0b0001001000000001", # T
"0b0000000000111110", # U
"0b0000110000110000", # V
"0b0010100000110110", # W
"0b0010110100000000", # X
"0b0001010100000000", # Y
"0b0000110000001001", # Z
"0b0000000000111001", # [
"0b0010000100000000", # \
"0b0000000000001111", # ]
"0b0000110000000011", # ^
"0b0000000000001000", # _
"0b0000000100000000", # `
"0b0001000001011000", # a
"0b0010000001111000", # b
"0b0000000011011000", # c
"0b0000100010001110", # d
"0b0000100001011000", # e
"0b0000000001110001", # f
"0b0000010010001110", # g
"0b0001000001110000", # h
"0b0001000000000000", # i
"0b0000000000001110", # j
"0b0011011000000000", # k
"0b0000000000110000", # l
"0b0001000011010100", # m
"0b0001000001010000", # n
"0b0000000011011100", # o
"0b0000000101110000", # p
"0b0000010010000110", # q
"0b0000000001010000", # r
"0b0010000010001000", # s
"0b0000000001111000", # t
"0b0000000000011100", # u
"0b0010000000000100", # v
"0b0010100000010100", # w
"0b0010100011000000", # x
"0b0010000000001100", # y
"0b0000100001001000", # z
"0b0000100101001001", # {
"0b0001001000000000", # |
"0b0010010010001001", # }
"0b0000010100100000", # ~
"0b0011111111111111"]



def convert_bin(lettre_in):

    CHAR_OUT=[]


    index_alphabet=33
    index_defaut=0
    for lettre in alphabet :
        if lettre_in == lettre :
            index_defaut=index_alphabet


        index_alphabet+=1
        CHAR_OUT=list(CHARS[index_defaut])
    return (CHAR_OUT)




def morph(lettre_in,lettre_out,compteur):


    CHAR_IN=list(lettre_in)
    CHAR_OUT=list(lettre_out)

    str1 = ""
    str2 = ""
    if CHAR_IN[compteur]!=CHAR_OUT[compteur]:
        if CHAR_IN[compteur]=='0':
            CHAR_IN[compteur]='1'
            return CHAR_IN



        elif CHAR_IN[compteur]=='1':
            CHAR_IN[compteur]='0'

            return CHAR_IN

    else :

        return CHAR_IN









def jam():
    for x in range (0,5) :
        if lettre_pre[0]!=' ':
            display1.set_digit_raw(0,random.randint(0,65535))
        if lettre_pre[1]!=' ':
            display1.set_digit_raw(1, random.randint(0,65535))
        if lettre_pre[2]!=' ':
            display1.set_digit_raw(2, random.randint(0,65535))
        if lettre_pre[3]!=' ':
            display1.set_digit_raw(3, random.randint(0,65535))

        if lettre_pre[4]!=' ':
            display2.set_digit_raw(0, random.randint(0,65535))
        if lettre_pre[5]!=' ':
            display2.set_digit_raw(1, random.randint(0,65535))
        if lettre_pre[6]!=' ':
            display2.set_digit_raw(2, random.randint(0,65535))
        if lettre_pre[7]!=' ':
            display2.set_digit_raw(3, random.randint(0,65535))


        if lettre_ism[0]!=' ':
            display3.set_digit_raw(1, random.randint(0,65535))
        if lettre_ism[1]!=' ':
            display3.set_digit_raw(2, random.randint(0,65535))
        if lettre_ism[2]!=' ':
            display3.set_digit_raw(3, random.randint(0,65535))

        if lettre_ism[3]!=' ':
            display4.set_digit_raw(0, random.randint(0,65535))
        if lettre_ism[4]!=' ':
            display4.set_digit_raw(1, random.randint(0,65535))
        if lettre_ism[5]!=' ':
            display4.set_digit_raw(2, random.randint(0,65535))
        if lettre_ism[6]!=' ':
            display4.set_digit_raw(3, random.randint(0,65535))

        if lettre_ism[7]!=' ':
            display5.set_digit_raw(0, random.randint(0,65535))
        if lettre_ism[8]!=' ':
            display5.set_digit_raw(1, random.randint(0,65535))
        if lettre_ism[9]!=' ':
            display5.set_digit_raw(2, random.randint(0,65535))
        if lettre_ism[10]!=' ':
            display5.set_digit_raw(3, random.randint(0,65535))

        if lettre_ism[11]!=' ':
            display6.set_digit_raw(0, random.randint(0,65535))
        if lettre_ism[12]!=' ':
            display6.set_digit_raw(1, random.randint(0,65535))
        if lettre_ism[13]!=' ':
            display6.set_digit_raw(2, random.randint(0,65535))
        if lettre_ism[14]!=' ':
            display6.set_digit_raw(3, random.randint(0,65535))
        time.sleep(0.1)





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
#    print(list_ism[index_ism])
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
#    print(list_pre[index_pre])
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


while True :

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


        for x in range(0,18):
            for y in range (8):

                pre_bin_in[y]=morph(pre_bin_in[y],pre_bin_out[y],x)
            for y in range (15):

                ism_bin_in[y]=morph(ism_bin_in[y],ism_bin_out[y],x)


            s=''
            if display1_connect:
                display1.set_digit_raw(0,int(s.join(pre_bin_in[0]),2))
                display1.set_digit_raw(1,int(s.join(pre_bin_in[1]),2))
                display1.set_digit_raw(2,int(s.join(pre_bin_in[2]),2))
                display1.set_digit_raw(3,int(s.join(pre_bin_in[3]),2))
            if display2_connect:
                display2.set_digit_raw(0,int(s.join(pre_bin_in[4]),2))
                display2.set_digit_raw(1,int(s.join(pre_bin_in[5]),2))
                display2.set_digit_raw(2,int(s.join(pre_bin_in[6]),2))
                display2.set_digit_raw(3,int(s.join(pre_bin_in[7]),2))
            if display3_connect:
                display3.set_digit_raw(1,int(s.join(ism_bin_in[0]),2))
                display3.set_digit_raw(2,int(s.join(ism_bin_in[1]),2))
                display3.set_digit_raw(3,int(s.join(ism_bin_in[2]),2))
            if display4_connect:
                display4.set_digit_raw(0,int(s.join(ism_bin_in[3]),2))
                display4.set_digit_raw(1,int(s.join(ism_bin_in[4]),2))
                display4.set_digit_raw(2,int(s.join(ism_bin_in[5]),2))
                display4.set_digit_raw(3,int(s.join(ism_bin_in[6]),2))
            if display5_connect:
                display5.set_digit_raw(0,int(s.join(ism_bin_in[7]),2))
                display5.set_digit_raw(1,int(s.join(ism_bin_in[8]),2))
                display5.set_digit_raw(2,int(s.join(ism_bin_in[9]),2))
                display5.set_digit_raw(3,int(s.join(ism_bin_in[10]),2))
            if display6_connect:
                display6.set_digit_raw(0,int(s.join(ism_bin_in[11]),2))
                display6.set_digit_raw(1,int(s.join(ism_bin_in[12]),2))
                display6.set_digit_raw(2,int(s.join(ism_bin_in[13]),2))
                display6.set_digit_raw(3,int(s.join(ism_bin_in[14]),2))
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
            display1.print(''.join(mot1_list))
        if display2_connect:
            display2.print(''.join(mot2_list))
        if display3_connect:
            display3.print(''.join(mot3_list))
        if display4_connect:
            display4.print(''.join(mot4_list))
        if display5_connect:
            display5.print(''.join(mot5_list))
        if display6_connect:
            display6.print(''.join(mot6_list))
        time.sleep(3)

    else :

        if display1_connect:
            display1.set_digit_raw(0,int("0b0011111111111111",2))
            display1.set_digit_raw(1,int("0b0011111111111111",2))
            display1.set_digit_raw(2,int("0b0011111111111111",2))
            display1.set_digit_raw(3,int("0b0011111111111111",2))
        if display2_connect:
            display2.set_digit_raw(0,int("0b0011111111111111",2))
            display2.set_digit_raw(1,int("0b0011111111111111",2))
            display2.set_digit_raw(2,int("0b0011111111111111",2))
            display2.set_digit_raw(3,int("0b0011111111111111",2))
        if display3_connect:
            display3.set_digit_raw(0,int("0b0011111111111111",2))
            display3.set_digit_raw(1,int("0b0011111111111111",2))
            display3.set_digit_raw(2,int("0b0011111111111111",2))
            display3.set_digit_raw(3,int("0b0011111111111111",2))
        if display4_connect:
            display4.set_digit_raw(0,int("0b0011111111111111",2))
            display4.set_digit_raw(1,int("0b0011111111111111",2))
            display4.set_digit_raw(2,int("0b0011111111111111",2))
            display4.set_digit_raw(3,int("0b0011111111111111",2))
        if display5_connect:
            display5.set_digit_raw(0,int("0b0011111111111111",2))
            display5.set_digit_raw(1,int("0b0011111111111111",2))
            display5.set_digit_raw(2,int("0b0011111111111111",2))
            display5.set_digit_raw(3,int("0b0011111111111111",2))
        if display6_connect:
            display6.set_digit_raw(0,int("0b0011111111111111",2))
            display6.set_digit_raw(1,int("0b0011111111111111",2))
            display6.set_digit_raw(2,int("0b0011111111111111",2))
            display6.set_digit_raw(3,int("0b0011111111111111",2))
        time.sleep(3)
        if display1_connect:
            display1.print("1111")
        if display2_connect:
            display2.print("2222")
        if display3_connect:
            display3.print("3333")
        if display4_connect:
            display4.print("4444")
        if display5_connect:
            display5.print("5555")
        if display6_connect:
            display6.print("6666")
        time.sleep(3)
