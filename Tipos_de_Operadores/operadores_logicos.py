# AND= para ser verdadeiro tudo tem que ser True
# OR= para ser verdadeiro apenas um tem que ser True


print (True and True)
print (True and False)
print (False and False)
print (True or True)
print (True or False)
print (False or False)



saldo = 1000
saque = 250
limite = 200
conta_especiaal = True


exp_1 = saldo >= saque and saque <= limite or conta_especiaal and saldo >= saque
print (exp_1)


exp_2 = (saldo >= saque and saque <= limite) or (conta_especiaal and saldo >= saque)
print (exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente= conta_especiaal and saldo >= saque

exp_3= (conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente)
print (exp_3)