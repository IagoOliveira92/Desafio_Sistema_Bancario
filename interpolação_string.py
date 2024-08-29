nome = "Camila"
idade = 33
profissao = "Mulher troféu"
signo = "Aries"
salario = 6000,687

dados = {"nome": "Iago", "idade": 30}

print("Nome: %s Idade: %d" %(nome, idade,)) #primeira

print("Nome: {} Idade: {}".format(nome, idade)) #segunda
print("Nome: {0} Idade: {1}".format(nome, idade))

print("Nome: {nome} Idade: {idade}".format(nome=nome,idade=idade)) #terceira
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))


print(f"Nome: {nome}, Idade: {idade}, Salário: {salario}")#quarto
"""print(f"Nome: {nome}, Idade: {idade}, Salário: {salario:.2f}")
"""

