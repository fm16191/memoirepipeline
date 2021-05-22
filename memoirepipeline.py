import os
import sys

# 4 bancs d'essais, 4T, fonction accès mémoires, n itérations

if not len(sys.argv) == 6:
    print("Mauvais arguments")
    exit()

try:
    bancs = sys.argv[1]
    T = int(sys.argv[2])
    n = int(sys.argv[3])

    fonctions = []
    for i in sys.argv[4].split(","):
        fonctions.append([int(i.split("i")[0]) if not i[0]== "i" else 1, int(i.split("+")[-1]) if "+" in i else 0])

    vecteur_init = [int(i) for i in sys.argv[5].split(",")]
except:
    print("Mauvais arguments")
    exit()

# bancs = 4
banc = [[],[],[],[]]
# T = 4
# fonctions = [[1,0],[2,1],[2,0]]
# vecteur_init = [0,3,0]
patterns = []
# n = 1000
# lettres = ["A","B","C"]
lettres = [chr(ord('A')+i) for i in range(len(fonctions))]
# print(lettres)

str_i = "            i ❯ "
str_banc = "position banc ❯ "

def aff_banc():
    print("|" + "|".join([f"{i:03d}" for i in range(len(banc[0]))]) + "|")
    for i in range(len(banc)):
        print("|" + "|".join(banc[i]) + "|")

it = 0
for i in range(0, n):
    str_i += "(" + ",".join([str(fonctions[j][0]*i+fonctions[j][1]) for j in range(3)]) + ")"
    str_banc += "(" + ",".join([str(fonctions[j][0]*i+fonctions[j][1] + vecteur_init[j]) for j in range(3)]) + ")"
    str_i += " - "
    str_banc += " - "

    save_it = it
    pattern = []
    for j in range(len(fonctions)):
        str_v = lettres[j] + f"{fonctions[j][0]*i+fonctions[j][1]:02d}"
        for k in range(len(banc)):
            while(len(banc[k])<=it+3):
                banc[k].append("   ")

        position = (fonctions[j][0]*i+fonctions[j][1] + vecteur_init[j]) % 4
        # print(banc[position])
        # print(position, it)
        # print(banc[position])
        # aff_banc()
        # print("------")
        # input()
        while(banc[position][it] != "   "):
            it += 1
            for k in range(len(banc)):
                banc[k].append("   ")

        for k in range(it, it+4):
            banc[position][k] = str_v


        it += 1
        pattern.append([position, it-save_it])
    if pattern in patterns:
        
        str_op = ""
        for k in range(len(fonctions)):
            str_op += lettres[k] + "["
            str_op += str(fonctions[k][0]) + "i" if fonctions[k][0] != 1 else "i"
            str_op += f"+{fonctions[k][1]}]" if fonctions[k][1] else "]"
            
        str_op = "], ".join(str_op.split("]"))
        print("===============",str_op[:-2], f"== n={n} == init", vecteur_init,"===============")

        print(str_i[:-3])
        print(str_banc[:-3])
        print("")
        aff_banc()

        temps_it = save_it-1
        while(banc[patterns[-1][-1][0]][save_it-1] == banc[patterns[-1][-1][0]][temps_it]):
            temps_it += 1

        print(f"\nPattern trouvé entre itérations {patterns.index(pattern)} et {len(patterns)}")
        print("Temps_initial:", temps_it)
        rendement_max = save_it - patterns[patterns.index(pattern)][0][1] + 1
        decalage_iterations = patterns.index(pattern)
        nb_iterations = len(patterns)-patterns.index(pattern)
        print("Rendement_max:", rendement_max)
        print("Itérations:", nb_iterations)
        latence = f"{rendement_max/nb_iterations}"
        latence += f"(n-{decalage_iterations})" if decalage_iterations else "n"
        latence += f"+{temps_it-rendement_max}"
        print("Latence:", latence)
        print("Temps exécution:", float(rendement_max/nb_iterations)*float(n-decalage_iterations)+float(temps_it-rendement_max),"T")
        break
    patterns.append(pattern)
