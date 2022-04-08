#saisie de l'utilisateur
from calendar import c


text_in = input("entrez votre texte: ")
cle_in = input("entrez votre clé: ")


#definition des variables
compteur = 0
compteur_text2 = 0
compteurasci_cle = 0
compteurasci_text = 0 
asci_text = []
asci_cle = []
asci_final = []
compteur_convert  = 0
text_chiffre = []
caractere_chiffre = 0



#convertir la clé en ascii et mets dans une liste
for cle_i in cle_in:
    asci_cle.insert(compteurasci_cle, ord(cle_i))
    #print(asci_cle)
    compteurasci_cle = compteurasci_cle + 1

#covertir le text en ascii et mets dans une liste
for text_i in text_in:
    """
    if ord(text_i) == 32:
        asci_text.insert(compteurasci_text, " ")
        compteurasci_text = compteurasci_text + 1
    else:
        print("je passe")
        asci_text.insert(compteurasci_text, ord(text_i))
        #print(ord(text_i))
        #print("-------------------------")
        compteurasci_text = compteurasci_text + 1
    """
    asci_text.insert(compteurasci_text, ord(text_i))
    #print(ord(text_i))
    #print("-------------------------")
    compteurasci_text = compteurasci_text + 1
print(asci_text)

"""
if compteurasci_text < compteurasci_cle :
    print("pute")
    compteurasci_total =  compteurasci_cle / compteurasci_text
    print(compteurasci_total)
else:
    print("bob")
    compteurasci_total = compteurasci_text / compteurasci_cle
    print(compteurasci_total)
"""
if compteurasci_text < compteurasci_cle :
    compteurasci_total =  compteurasci_cle 

else:
    compteurasci_total = compteurasci_text

#gros c carré je l'ai reconverti en caracteres pour voir et il me sort sa : ['\x04', '\x16', '\x0c', '\x19', '\x02', '\x07']


#chiffre le texte
for x in range(compteurasci_total):

    #regarde si c'est un espace si oui le converti pas
    if asci_text[compteur_text2] == 32:
        text_chiffre.insert(x, " ")
        compteur_text2 = compteur_text2 + 1

    #si ce n'est pas un espace le converti
    else:
        caractere_chiffre = (asci_text[x] + asci_cle[x])%26
        #caractere_chiffre = chr(caractere_chiffre)
        print(caractere_chiffre)
        #mets le calcul dans la variable
        text_chiffre.insert(compteur_text2, caractere_chiffre)
        compteur_text2 = compteur_text2 + 1
    print("------------------")
    print(text_chiffre)


#passe le texte chiffré en caractères

# print(asci_cle)
# print(asci_text)
# print("----------------")
# print(text_chiffre)


#text_chiffre = (asci_cle + asci_text)%26

#print(text_chiffre)
print("---------------")
print(text_in)
print("---------------")
