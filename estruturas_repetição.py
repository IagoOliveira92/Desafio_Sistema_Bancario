texto =input("Informe um texto: ")

VOGAIS = "EAIOU"

#exemplo c/ iteração
for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra, end="")

else: 
    print()
    print("final do laço!")

 #exemplo c/ range
for numero in range(0,51,5): 
    print(numero, end=" ")


#exemplo c/ while
opcao = -1 

while opcao != 0: 
    opcao = int(input("[1] Sacar \n [2] Extrato \n[0] Sair \n: "))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

#exemplo c/ break
while True:
    numero = int(input("Informe um número: "))
    if numero == 10:
        break
    print(numero)

nome = "IAGO LUCIAN DE JESUS OLIVEIRA"

