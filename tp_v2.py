# importation des lib
import argparse

# Creation du -h et des commande
# Creation de la description pour le help
parser = argparse.ArgumentParser(description="Programme de chiffrage Vignere")
# creation des argument pour le help
# argument pour le fhciher a chiffre/dechiffre
parser.add_argument('-e', '--fichierEntre', type=str,
                    help="Fichier dans lequel se trouve le message a chiffré", metavar="", required=True)
# argument pour donner la cles de chiffrement
parser.add_argument('-k',  '--clef', type=str,
                    help="Clef de chiffrage", metavar="", required=True)
# argument pour le ficher chiffre/dechiffre
parser.add_argument('-s', '--fichierSortie', type=str,
                    help="Fichier dans lequel se trouvera le message chiffré", metavar="", required=True)
# argument pour dire qu'on doit chiffre
parser.add_argument('-c', '--chiffrement', action='store_true',
                    help="chiffrer un texte")
# argument pour dire qu'on doit dechiffre
parser.add_argument('-d', '--dechiffrement', action='store_true',
                    help="déchiffrer un texte")
args = parser.parse_args()

# ouver du ficher de l'argument -e en utf8
f = open(args.fichierEntre, "r", encoding='utf8')
# mettre tout le text du fhicher -e dans la variable text_in
text_in = f.read()
# mettre la cle de l'argument -k dans la variable cle_in
cle_in = args.clef

# definition des variables pour l'alphabe
# mettre a l'alphaber en minuscule dans la variable alpa_mi
alpha_mi = "abcdefghijklmnopqrstuvwxyz"
# mettre a l'alphaber en majuscule dans la variable alpa_ma
alpha_ma = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# definition des variables pour les calcul
# creation d'une variable int
runMessage = 0
# creation d'une variable int
runCle = 0
# creation d'une liste
tabl_chif = []
# creation d'une variable string
caractere_text = ""
# creation d'une variable string
caractere_cle = ""
# creation d'une variable string
caractere_cles = ""
# creation d'une variable string
caractere_chiffre = ""
# creation d'une variable string
tabl_final = ""

#faire que si l'argument -c est utiliser alors chiffre le text
if args.chiffrement == True:
    # entre dans la boucle si le text a pas fini de ce chiffre
    while runMessage < len(text_in):
        # revien au debut de la cle si le text et plus grand que la cle
        if runCle == len(cle_in):
            # remettre le compteur de la cle a 0
            runCle = 0
        # crypte la lettre is dans le text elle est minuscule et dans la cle aussi
        if ord(text_in[runMessage]) > 96 and ord(text_in[runMessage]) < 123 and ord(cle_in[runCle]) > 96 and ord(cle_in[runCle]) < 123:
            for x in alpha_mi:
                alpha_mi.index(x)
                if x == text_in[runMessage]:
                    caractere_text = alpha_mi.index(x)
                    caractere_cle = cle_in[runCle]
                    caractere_cles = alpha_mi.index(caractere_cle)
                    caractere_chiffre = (caractere_text + caractere_cles) % 26
                    tabl_chif.insert(runMessage, caractere_chiffre)
                    tabl_final += alpha_mi[tabl_chif[runMessage]]
                    break
        # crypte la lettre is dans le text elle est minuscule et la cle est majucule
        elif ord(text_in[runMessage]) > 96 and ord(text_in[runMessage]) < 123 and ord(cle_in[runCle]) > 64 and ord(cle_in[runCle]) < 91:
            for i in alpha_mi:
                alpha_mi.index(i)
                if i == text_in[runMessage]:
                    caractere_text = alpha_mi.index(i)
                    caractere_cle = cle_in[runCle]
                    caractere_cles = alpha_ma.index(caractere_cle)
                    caractere_chiffre = (caractere_text + caractere_cles) % 26
                    tabl_chif.insert(runMessage, caractere_chiffre)
                    tabl_final += alpha_mi[tabl_chif[runMessage]]
                    break
        # crypte la lettre is dans le text elle est majucule et la cle est minuscule
        elif ord(text_in[runMessage]) > 64 and ord(text_in[runMessage]) < 91 and ord(cle_in[runCle]) > 96 and ord(cle_in[runCle]) < 123:
            for n in alpha_ma:
                alpha_ma.index(n)
                if n == text_in[runMessage]:
                    caractere_text = alpha_ma.index(n)
                    caractere_cle = cle_in[runCle]
                    caractere_cles = alpha_mi.index(caractere_cle)
                    caractere_chiffre = (caractere_text + caractere_cles) % 26
                    tabl_chif.insert(runMessage, caractere_chiffre)
                    tabl_final += alpha_ma[tabl_chif[runMessage]]
                    break
        # crypte la lettre is dans le text elle est majucule et dans la cles aussi
        elif ord(text_in[runMessage]) > 64 and ord(text_in[runMessage]) < 91 and ord(cle_in[runCle]) > 64 and ord(cle_in[runCle]) < 91:
            for y in alpha_ma:
                alpha_ma.index(y)
                if y == text_in[runMessage]:
                    caractere_text = alpha_ma.index(y)
                    caractere_cle = cle_in[runCle]
                    caractere_cles = alpha_ma.index(caractere_cle)
                    caractere_chiffre = (caractere_text + caractere_cles) % 26
                    tabl_chif.insert(runMessage, caractere_chiffre)
                    tabl_final += alpha_ma[tabl_chif[runMessage]]
                    break
        # lesse les caracter speciaux
        else:
            tabl_chif.insert(runMessage, text_in[runMessage])
            tabl_final += text_in[runMessage]
        runMessage = runMessage + 1
        runCle = runCle + 1
    f = open(args.fichierSortie, "w", encoding='utf8')
    f.write(tabl_final)
    print("Votre code a bien été chiffré")

elif args.dechiffrement == True:
    while runMessage < len(text_in):
        # revien au debut de la cle si le text na pas fini de ce crypter
        if runCle == len(cle_in):
            runCle = 0
        # crypte la lettre il dans le text elle est minuscule et dans la cle aussi
        if ord(text_in[runMessage]) > 96 and ord(text_in[runMessage]) < 123 and ord(cle_in[runCle]) > 96 and ord(cle_in[runCle]) < 123:
            for x in alpha_mi:
                alpha_mi.index(x)
                if x == text_in[runMessage]:
                    caractere_text = alpha_mi.index(x)
                    caractere_cle = cle_in[runCle]
                    caractere_cles = alpha_mi.index(caractere_cle)
                    caractere_chiffre = (caractere_text - caractere_cles) % 26
                    tabl_chif.insert(runMessage, caractere_chiffre)
                    tabl_final += alpha_mi[tabl_chif[runMessage]]
                    break
        # crypte la lettre il dans le text elle est minuscule et la cle est majucule
        elif ord(text_in[runMessage]) > 96 and ord(text_in[runMessage]) < 123 and ord(cle_in[runCle]) > 64 and ord(cle_in[runCle]) < 91:
            for i in alpha_mi:
                alpha_mi.index(i)
                if i == text_in[runMessage]:
                    caractere_text = alpha_mi.index(i)
                    caractere_cle = cle_in[runCle]
                    caractere_cles = alpha_ma.index(caractere_cle)
                    caractere_chiffre = (caractere_text - caractere_cles) % 26
                    tabl_chif.insert(runMessage, caractere_chiffre)
                    tabl_final += alpha_mi[tabl_chif[runMessage]]
                    break
        # crypte la lettre il dans le text elle est majucule et la cle est minuscule
        elif ord(text_in[runMessage]) > 64 and ord(text_in[runMessage]) < 91 and ord(cle_in[runCle]) > 96 and ord(cle_in[runCle]) < 123:
            for n in alpha_ma:
                alpha_ma.index(n)
                if n == text_in[runMessage]:
                    caractere_text = alpha_ma.index(n)
                    caractere_cle = cle_in[runCle]
                    caractere_cles = alpha_mi.index(caractere_cle)
                    caractere_chiffre = (caractere_text - caractere_cles) % 26
                    tabl_chif.insert(runMessage, caractere_chiffre)
                    tabl_final += alpha_ma[tabl_chif[runMessage]]
                    break
        # crypte la lettre il dans le text elle est majucule et dans la cles aussi
        elif ord(text_in[runMessage]) > 64 and ord(text_in[runMessage]) < 91 and ord(cle_in[runCle]) > 64 and ord(cle_in[runCle]) < 91:
            for y in alpha_ma:
                alpha_ma.index(y)
                if y == text_in[runMessage]:
                    caractere_text = alpha_ma.index(y)
                    caractere_cle = cle_in[runCle]
                    caractere_cles = alpha_ma.index(caractere_cle)
                    caractere_chiffre = (caractere_text - caractere_cles) % 26
                    tabl_chif.insert(runMessage, caractere_chiffre)
                    tabl_final += alpha_ma[tabl_chif[runMessage]]
                    break
        # lesse les caracter speciaux
        else:
            tabl_chif.insert(runMessage, text_in[runMessage])
            tabl_final += text_in[runMessage]
        runMessage = runMessage + 1
        runCle = runCle + 1

    f = open(args.fichierSortie, "w", encoding='utf8')
    f.write(tabl_final)
    print("Votre code a bien été dechiffré")
# print(tabl_chif)
# print(tabl_final)
