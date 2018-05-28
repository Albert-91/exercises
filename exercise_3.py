from itertools import cycle

def rot13(s):
    # l = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    # l = list(l)
    # s = list(s.lower())
    # NewS = []
    # for i in s:
    #     upper = i.isupper()
    #     indeks = (int(l.index(i)) + 13) % 26
    #     NewS.append(l[indeks])
    # return ''.join(NewS)
#or
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_s = ''
    for ch in s:
        upper = ch.isupper()
        try:
            index = (alphabet.index(ch.lower()) + 13) % 26
        except ValueError:
            new_s += ch
        else:
            new_ch = alphabet[index]
            if upper:
                new_ch = new_ch.upper()
            new_s += new_ch
    return new_s

print(rot13("Ala ma kota"))
print(rot13("Obal"))

#bony

from codecs import encode

print(encode("Ala ma kota", 'rot_13'))
