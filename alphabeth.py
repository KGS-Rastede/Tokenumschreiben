ersetzungstabelle = {
    "A" : "Anton",
    "B" : "Berta",
    "C" : "Caesar",
    "D" : "Dora",
    "E" : "Emil",
    "F" : "Friedrich",
    "G" : "Gustav",
    "H"	: "Heinrich",
    "I" : "Ida",
    "J" : "Julius",
    "K" : "Konrad",
    "L" : "Ludwig",
    "M" : "Martha",
    "N" : "ordpol",
    "O" : "Otto",
    "P" : "Paula",
    "Q" : "Quelle",
    "R" : "Richard",
    "S" : "Siegfried",
    "T" : "Theodor",
    "U" : "Ulrich",
    "V" : "Viktor",
    "W" : "Wilhelm",
    "X" : "Xanthippe",
    "Y" : "Ypsilon",
    "Z" : "Zeppelin",
    "a" : "anton",
    "b" : "berta",
    "c" : "caesar",
    "d" : "dora",
    "e" : "emil",
    "f" : "friedrich",
    "g" : "gustav",
    "h" : "heinrich",
    "i" : "ida",
    "j" : "julius",
    "k" : "konrad",
    "l" : "ludwig",
    "m" : "martha",
    "n" : "nordpol",
    "o" : "otto",
    "p" : "paula",
    "q" : "quelle",
    "r" : "richard",
    "s" : "siegfried",
    "t" : "theodor",
    "u" : "ulrich",
    "v" : "viktor",
    "w" : "wilhelm",
    "x" : "xanthippe",
    "y" : "ypsilon",
    "z" : "zeppelin",
    "0" : "Null",
    "1" : "Eins",
    "2" : "Zwei",
    "3" : "Drei",
    "4" : "Vier",
    "5" : "Fünf",
    "6" : "Sechs",
    "7" : "Sieben",
    "8" : "Acht",
    "9" : "Neun",
    "#" : "#"
    }

def alphabet(token):
    z = ""
    for zeichen in token:
        z += ersetzungstabelle[zeichen]
        z += "-"
        
    return z
        

zieldatei = open('ergebnis.txt', 'a+')
        
        
with open('tokens.txt') as datei:
    token = datei.readlines()
    
    token.pop(0)
       
       
    for t in token:
        foo = t.rstrip()
        zeile = foo + ", " + alphabet(foo)
        zieldatei.write(zeile + "\n")
