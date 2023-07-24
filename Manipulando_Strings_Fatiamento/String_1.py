nome = "juLiana"

#deixar todas maiusculas
print(nome.upper())
#deixar todas minusculas
print(nome.lower())
# deixar somente a primeira letra maiuscula
print(nome.title())


texto = "  Bem vinda!    "

print(texto)
#tira o espaço em branco
print(texto.strip())
#tira o espaço somente da esquerda
print(texto.lstrip())
#tira o espaço somente da direita
print(texto.rstrip())


menu = "Ferramenta"
 
print("###" + menu + "###")
print(menu.center(16))
print(menu.center(16 , "#"))

# Separar as letras com traço F-e-r-r-a-m-e-n-t-a
print("-".join(menu))