#!/usr/bin/python3
import random
a = 10
b = 5
print(a+b)

# ceci est un commentaire sur une ligne

age = "je suis vieux"

print(age)

age = "je suis jeune"
print(age)

text = "je suis du text"
print(type(text))

nombre = 42

print(type(nombre))

print(text * 3)
#concatenation

text = text + "en plus"

print(text)
txt = "Hello World !!!"
print(len(txt))

print(txt[1])
print(txt[0:5])
print("bonjour je m'appelle %s" %("Mehdi"))

text = "je suis du \"texte\""
print(text)

# Liste

maListe = []
print(type(maListe))
maListe = [1,2,3]
print(maListe)

maListe = []
maListe.append(1)
print(maListe)
maListe.append("salut")
print(maListe)


def test():

# Supprimé avec l'index
del maListe[1]
print(maListe)

# supprimé avec la valeur
maListe.remove("troisieme")


maListe = ["1er", "deuxieme", "troisieme"]
print(maListe[1])
print(maListe[2])
maListe[1] = "changement"
print(maListe)

