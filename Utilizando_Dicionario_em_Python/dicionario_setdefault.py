contato = {"nome":"Juliana Souza", "telefone": "13-99999-9999"}
   

contato.setdefault("nome", "Rodrigo") #{'nome': 'Juliana Souza', 'telefone': '13-99999-9999'}
print(contato)

contato.setdefault("idade", 36) #{'nome': 'Juliana Souza', 'telefone': '13-99999-9999', 'idade': 36}
print(contato)