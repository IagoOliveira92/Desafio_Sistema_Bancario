def criar_carro(modelo, ano, placa, /, marca, motor,combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("palio",2012, "IAC/9192", marca="fiat", motor="2.0", combustivel="gasolina" ) #valido

#criar_carro(modelo="GOL",ano=2025, placa="CAI-9119", marca="Volkswagem", motor="1.6", combustivel="Flex") #invalido 
