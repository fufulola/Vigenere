text_in = input("entrez votre texte: ")
cle_in = input("entrez votre clé: ")

compteur = 0
compteurasci_cle = 0
compteurasci_text = 0 
asci_text = []
asci_cle = []
asci_final = []

for cle_i in cle_in:
    asci_cle.insert(compteurasci_cle, ord(cle_i))
    #print(asci_cle)
    compteurasci_cle = compteurasci_cle + 1


for text_i in text_in:
    asci_text.insert(compteurasci_text, ord(text_i))
    #print(ord(text_i))
    #print("-------------------------")
    compteurasci_text = compteurasci_text + 1

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

for i in compteurasci_total:
    




print(asci_cle)
print(asci_text)


  
#text_chiffre = (asci_cle + asci_text)%26


#print(text_chiffre)

    


print(text_in)
print("---------------")





