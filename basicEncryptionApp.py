def crypted(sentence):
    translation=""
    for element in sentence:
        if element in "Aa":
            translation=translation+"1"
        elif element in "Bb":
            translation=translation+"2"
        elif element in"Cc":
            translation+='@'
        elif element in "Dd":
            translation=translation+"!"
        elif element in"Ee":
            translation+='5'
        elif element in "Ff":
            translation=translation+"#"
        elif element in"Gg":
            translation+='$'
        elif element in "Hh":
            translation=translation+"%"
        elif element in"Ii":
            translation+='('
        elif element in "Jj":
            translation=translation+"0"
        elif element in"Kk":
            translation+='^'
        elif element in "Ll":
            translation=translation+"+"
        elif element in"Mm":
            translation+='-' 
        elif element in "Nn":
            translation=translation+")"
        elif element in"Oo":
            translation+='*'
        elif element in "Pp":
            translation=translation+"{"
        elif element in"Qq":
            translation+='}'
        elif element in "Rr":
            translation=translation+"/"
        elif element in"Ss":
            translation+='='
        elif element in "Tt":
            translation=translation+"~"
        elif element in"Uu":
            translation+='8'
        elif element in "Vv":
            translation=translation+"8"
        elif element in"Ww":
            translation+='6'
        elif element in "Xx":
            translation=translation+"<"
        elif element in"Yy":
            translation+=',' 
        elif element in "Zz":
            translation+="?"               
        else:
            translation+=element
    return translation

print(crypted(input("What do you want to crypt : ")))