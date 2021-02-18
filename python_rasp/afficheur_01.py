import board
import time
import string
from adafruit_ht16k33.segments import Seg14x4

i2c = board.I2C()
display1 = Seg14x4(i2c, address=0x70)
display2 = Seg14x4(i2c, address=0x71)
display3 = Seg14x4(i2c, address=0x72)
display4 = Seg14x4(i2c, address=0x73)
display5 = Seg14x4(i2c, address=0x74)
display6 = Seg14x4(i2c, address=0x75)

mot1= "AAAA"
mot2= "AAAA"
mot3= "AAAA"
mot4= "AAAA"
mot5= "AAAA"
mot6= "AAAA"
mot1_list = list(mot1)
mot2_list = list(mot2)
mot3_list = list(mot3)
mot4_list = list(mot4)
mot5_list = list(mot5)
mot6_list = list(mot6)


while True :

    for x in string.ascii_uppercase:

        mot1_list[0]=x
        mot1_list[1]=x
        mot1_list[2]=x
        mot1_list[3]=x

        mot2_list[0]=x
        mot2_list[1]=x
        mot2_list[2]=x
        mot2_list[3]=x

        mot3_list[0]=x
        mot3_list[1]=x
        mot3_list[2]=x
        mot3_list[3]=x

        mot4_list[0]=x
        mot4_list[1]=x
        mot4_list[2]=x
        mot4_list[3]=x

        mot5_list[0]=x
        mot5_list[1]=x
        mot5_list[2]=x
        mot5_list[3]=x

        mot6_list[0]=x
        mot6_list[1]=x
        mot6_list[2]=x
        mot6_list[3]=x

        display1.print(''.join(mot1_list))
        display2.print(''.join(mot2_list))
        display3.print(''.join(mot3_list))
        display4.print(''.join(mot4_list))
        display5.print(''.join(mot5_list))
        display6.print(''.join(mot6_list))
        time.sleep(0.5)

    display1.print("THOM")
    display2.print("AS G")
    display3.print("ARNI")
    display4.print("ER P")
    display5.print("U DU")
    display6.print(" CUL")
    time.sleep(1)
