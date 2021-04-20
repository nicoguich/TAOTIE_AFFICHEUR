
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
