MAIOR_IDADE= 18
IDADE_MENOR = 16

idade = int(input("Informe  sua idade: 16"))
 
if idade >= MAIOR_IDADE:
    print("Você esta apto para tirar a CNH...")

if idade < MAIOR_IDADE:
    print("Lamento você não esta apto!")



if idade >= MAIOR_IDADE:
    print("Você esta apto para tirar a CNH...")

else:
    print("Lamento você não esta apto!")



if idade >= MAIOR_IDADE:
    print("Você esta apto para tirar a CNH...")

elif idade == IDADE_MENOR:
     print("Menor de 18 anos pode partcipar nas aulas teóricas, mas não pode fazer aulas praticas...")

else:
    print("Lamento você não esta apto para tirar CNH!")
