def somar(a, b):
    return a + b
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"Resultado da operação {a} + {b} = {resultado}")

exibir_resultado(5, 5, somar)
