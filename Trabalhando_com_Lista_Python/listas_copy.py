lista = [1, "Juliana", [30,20,10]]

lista_2 = lista.copy() #[1, "Juliana", [30,20,10]]

print(id(lista_2) , id(lista))



lista_2[0] = 2

print(lista_2)
print(lista)