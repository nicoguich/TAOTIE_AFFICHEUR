
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
