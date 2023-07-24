nome = "Juliana"
idade = 36
profissao = "Qa"
linguagem = "Python"
saldo = "40.000"

dados = {"nome": "Juliana", "idade": "36"}

print("nome: %s, idade: %d " % (nome , idade))
print("nome: {}, idade: {} " .format (nome, idade))
print("nome: {1}, idade: {0} " .format (idade,nome))
print("nome: {nome}, idade: {idade} " .format (nome = nome, idade= idade))
print("nome: {name}, idade: {age} " .format (age=idade , name=nome))

print("nome: {nome}, idade: {idade} " .format (**dados))

print(f"nome: {nome}, idade: {idade}, saldo :{saldo}")
print(f"nome: {nome}, idade: {idade}, saldo :{saldo:10.2}")