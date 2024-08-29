conta_normal = False
conta_universitaria = True

saldo = 5000
saque = int(input("Informar valor de saque: "))
cheque_especial = 450

if conta_normal: 
    if saldo >= saque:
        print(f" O valor de R${saque}, foi sacado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com cheque especial!")
    else:
        print("Sem saldo para realizar essa operação! ")

if conta_universitaria:
    if saldo >= saque:
        print(f" O valor de R${saque}, foi sacado com sucesso!")
    else:
        print(f"Saldo insulficiente para realizar essa operação! Saldo atual é de: {saldo}")