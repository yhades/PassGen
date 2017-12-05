import string
from random import*
predvolba = string.hexdigits
heslo =  "".join(choice(predvolba) for delka in range(randint(6, 19)))
text = "Vygenerované heslo je: "
print("Tento python script generuje náhodná hesla s politikou velkých a malých písmen, čísel a rozsahem 6 - 19 znaků.")
print("=============================")
print(text + heslo)
print("=============================")
