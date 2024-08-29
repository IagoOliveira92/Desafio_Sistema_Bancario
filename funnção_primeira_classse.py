def somar(a,b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O valor desta operação é = {resultado}")

exibir_resultado(10, 5, somar)
exibir_resultado(10,2,subtrair)