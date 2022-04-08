#saisie de l'utilisateur
text_in = input("entrez votre texte: ")
cle_in = input("entrez votre clé: ")

#definition des variables pour l'alphabe
alpha_mi = "abcdefghijklnmopqrstuvwxyz"
alpha_ma = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"

#definition des variables pour les calcul
runmessage = 0
runcle = 0
tabl_chif = []
caractere_text = "";
caractere_cle = "";
caractere_cles = "";
caractere_chiffre = "";
tabl_final = "";

#entre dans la boucle si le text a pas fini de ce crypter
while runmessage < len(text_in):
    #reset runcle si la cle est plus court que le text
    if runcle == len(cle_in):
        runcle = 0
    if ord(text_in[runmessage]) > 96 and ord(text_in[runmessage]) < 123 and ord(cle_in[runcle]) > 96 and ord(cle_in[runcle]) < 123:
        for x in alpha_mi:
            alpha_mi.index(x)
            if x == text_in[runmessage]:
                caractere_text = alpha_mi.index(x)
                caractere_cle = cle_in[runcle]
                caractere_cles = alpha_mi.index(caractere_cle)
                caractere_chiffre = (caractere_text + caractere_cles)%26
                tabl_chif.insert(runmessage, caractere_chiffre)
                tabl_final += alpha_mi[tabl_chif[runmessage]]
    elif ord(text_in[runmessage]) > 96 and ord(text_in[runmessage]) < 123 and ord(cle_in[runcle]) > 64 and ord(cle_in[runcle]) < 91:
        for i in alpha_mi:
            alpha_mi.index(i)
            if i == text_in[runmessage]:
                caractere_text = alpha_mi.index(i)
                caractere_cle = cle_in[runcle]
                caractere_cles = alpha_ma.index(caractere_cle)
                caractere_chiffre = (caractere_text + caractere_cles)%26
                tabl_chif.insert(runmessage, caractere_chiffre)
                tabl_final += alpha_mi[tabl_chif[runmessage]]
    elif ord(text_in[runmessage]) > 64 and ord(text_in[runmessage]) < 91 and ord(cle_in[runcle]) > 96 and ord(cle_in[runcle]) < 123:
        for n in alpha_ma:
            alpha_ma.index(n)
            if n == text_in[runmessage]:
                caractere_text = alpha_ma.index(n)
                caractere_cle = cle_in[runcle]
                caractere_cles = alpha_mi.index(caractere_cle)
                caractere_chiffre = (caractere_text + caractere_cles)%26
                tabl_chif.insert(runmessage, caractere_chiffre)
                tabl_final += alpha_ma[tabl_chif[runmessage]]
    elif ord(text_in[runmessage]) > 64 and ord(text_in[runmessage]) < 91 and ord(cle_in[runcle]) > 64 and ord(cle_in[runcle]) < 91:
        for y in alpha_ma:
            alpha_ma.index(y)
            if y == text_in[runmessage]:
                caractere_text = alpha_ma.index(y)
                caractere_cle = cle_in[runcle]
                caractere_cles = alpha_ma.index(caractere_cle)
                caractere_chiffre = (caractere_text + caractere_cles)%26
                tabl_chif.insert(runmessage, caractere_chiffre)
                tabl_final += alpha_ma[tabl_chif[runmessage]]
    else:
        tabl_chif.insert(runmessage, text_in[runmessage])
        tabl_final += text_in[runmessage]
    runmessage = runmessage + 1
    runcle = runcle + 1
print(tabl_chif)
print(tabl_final)
