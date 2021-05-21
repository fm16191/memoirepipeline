import os
import sys

# 4 bancs d'essais, 4T, fonction accès mémoires, n itérations

bancs = 4
banc = [[],[],[],[]]
T = 4
fonctions = [[1,0],[2,1],[2,0]]
vecteur_init = [0,3,0]
n = 1000
lettres = ["A","B","C"]

str_i = ""
str_banc = ""

def aff_banc():
    # for i in range(len(banc[0])):
    print("|".join([f"{i:02d}" for i in range(len(banc[0]))]))
    for i in range(len(banc)):
        # print(banc[i])
        print("|".join(banc[i]) + "|")


it = 0
for i in range(0,5):
    if not str_i == "":
        str_i += " - "
    if not str_banc == "":
        str_banc += " - "
    str_i += "(" + ",".join([str(fonctions[j][0]*i+fonctions[j][1]) for j in range(3)]) + ")"
    str_banc += "(" + ",".join([str(fonctions[j][0]*i+fonctions[j][1] + vecteur_init[j]) for j in range(3)]) + ")"


    for j in range(len(fonctions)):
        str_v = lettres[j] + str(fonctions[j][0]*i+fonctions[j][1])
        for k in range(len(banc)):
            while(len(banc[k])<=it+3):
                banc[k].append("  ")
        # print(j, "j_i", i, "_", fonctions[j][0]*i+fonctions[j][1] + vecteur_init[j], 
        # (fonctions[j][0]*i+fonctions[j][1] + vecteur_init[j])%4)
        position = (fonctions[j][0]*i+fonctions[j][1] + vecteur_init[j]) % 4
        # print(banc[position])
        if banc[position][-2] != "  ":
            it+=3
            for k in range(len(banc)):
                while(len(banc[k])<=it+4):
                    banc[k].append("  ")
                    
        # print(position, it, len(banc[position]))
        banc[position][it] = str_v
        banc[position][it+1] = str_v
        banc[position][it+2] = str_v
        banc[position][it+3] = str_v
        it += 1
        # aff_banc()
        # input()
        
    # print(banc[j])

print(str_i)
print(str_banc)

aff_banc()
# print(banc)
