def lpc(list,janela):
    after_lpc = list[:janela]
    janela_atual = after_lpc[-janela:]
    resto = list[janela:]
    while(len(resto)>=janela):
        after_lpc+=getErro(janela_atual,resto[:janela])
        janela_atual = resto[-janela:]
        resto = resto[janela:]
    after_lpc+=getErro(janela_atual[-len(resto):],resto)
    return(after_lpc)

# print("ENTROPIA BWT+RLE: %0.3f"  %entropy(getFreqs(lpc(aux_list,12))))
