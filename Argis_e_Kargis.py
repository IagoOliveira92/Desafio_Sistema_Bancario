def exibir_poema(data_extenso,*args, **kargs):
    texto ="\n".join(args)
    meta_dados ="\n".join(f"[{chave.title()}: {valor}" for chave, valor in kargs.items()])
    print(mensagem)

    