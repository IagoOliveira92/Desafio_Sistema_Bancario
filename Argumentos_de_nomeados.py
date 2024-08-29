def salvar_carro(marca, modelo, ano, placa):
    #salvar carro no banco de dados! 
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("FIAT", "UNO", 1996, "IAC-9192")
salvar_carro(marca="Chery", modelo="Tiggo", ano=2025, placa="IAC-9192")
salvar_carro(**{"marca":"Honda", "modelo":"HRV", "ano":2025, "placa":"IAC-9192"})