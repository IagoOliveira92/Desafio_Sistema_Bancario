"""#Aplicação de IF símples:
maior_idade = 18
idade = int(input("Informe sua Idade: "))

if idade >= maior_idade:
    print("Aprovado, Você está apta para tirar CNH!")


if idade < maior_idade:
    print("Reprovado, Você ainda não pode tirar CNH!")
""""""
#Aplicação de IF/ELSE:
15

maior_idade = 18
idade = int(input("Informe sua Idade: "))

if idade >= maior_idade:
    print("Aprovado, Você está apta para tirar CNH!")
else:
    print("Reprovado, Você não tem idade para tirar CNH ainda! ")
"""

#aplicação IF/ELIF/ELSE

maior_idade = 18
idade_especial = 16
idade = int(input("Informe sua Idade: "))

if idade >= maior_idade:
    print("Aprovado, Você está apta para tirar CNH!")
elif idade == idade_especial:
    print("Você pode fazer apenas às aulas teoricas! ")
else:
    print("Reprovado, Você ainda não pode tirar CNH! ")