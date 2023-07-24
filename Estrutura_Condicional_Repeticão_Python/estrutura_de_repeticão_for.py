

#Utilizando iteravel
texto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end= "")

print()

#tabuada do 5 utilizando a função range
for numero in range(0, 51, 5):
    print(numero, end= " ")