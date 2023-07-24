contatos = {
    "fenixrodrigo@hotmail.com": {"nome": "Rodrigo Venceslau", "telefone": "13-97777-77-77"}
    }

print(contatos.get("chave")) #None

#Caso não encontrar a chave, ele dovolve um dicionario vazio{} do segundo argumentos
print(contatos.get("chave", {})) #{}

#Caso não encontrar a chave do e-mail, ele dovolve um dicionario vazio{} do segundo argumentos
print(contatos.get("fenixrodrigo@hotmail.com", {})) #{'nome': 'Rodrigo Venceslau', 'telefone': '13-97777-77-77'}