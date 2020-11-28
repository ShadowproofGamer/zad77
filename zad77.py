import math
#print(ord('\n')-65)
print(chr(10))

def szyfr(dane, klucz, rev=False):
    temp=""
    key = -1
    for i in range(len(dane)):

        literka = ord(dane[i])-65
        if literka >= 0:
            key += 1
            jump = ord(klucz[key % len(klucz)])-65
            if rev:
                temp += chr(((literka-jump+26) % 26) +65)
                #print("TEST: ", i, key, jump, literka, (literka-jump+26) % 26)
            else:
                temp += chr(((literka+jump) % 26)+65)

        else:
            temp += dane[i]
    return temp


plik1 = open("dokad.txt")
dane1 = plik1.read()

print(math.ceil(len(dane1)/len("LUBIMYCZYTAC")))
temp_info = szyfr(dane1, "LUBIMYCZYTAC")
print(temp_info)
plik2=open("odpowiedzi.txt", "w+")
plik2.write(temp_info+"\n")

plik3 = open("szyfr.txt")
dane2 = plik3.readline()
klucz = plik3.readline().strip()
#print(dane2, klucz)
print(szyfr(dane2, klucz, True))
plik2.write(szyfr(dane2, klucz, True)+"\n")

def liczba_liter(tekst):
    liczba_wystopien = []
    for j in range(ord('A'), ord('Z')+1, 1):
        liczba_wystopien.append(0)
    for i in tekst:
        if ord(i)>=65:
            liczba_wystopien[ord(i)-65] += 1
    return liczba_wystopien


odpowiedz_ile = liczba_liter(dane2)
def wypisywanie(tab):
    for i in range(len(tab)):
        print("liter " + chr(i + 65) + " jest: " + str(tab[i]))

wypisywanie(odpowiedz_ile)
def szacowana_dlugosc(tab):
    l = 0
    n = 0
    for i in tab:
        l += i*(i-1)
        n += i
    k = l/(n*(n-1))
    d = 0.0285/(k-0.0385)
    return round(d, 2)

print("szacunkowa dlugosc klucza: "+ str(szacowana_dlugosc(odpowiedz_ile)) + "\nrzeczywista dlugosc klucza: "+ str(len("LUBIMYCZYTAC")))



