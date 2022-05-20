

# Criando a função do click do botão
def btn_click(variavel):
    variavel = 'eita'
    return variavel

# função para pegar o centro do monitor e retornar no tadrão do tkinter
def center(janela, largura, altura):
    janela = janela
    largura = largura
    altura = altura
    largura_screen = janela.winfo_screenwidth()
    altura_screen = janela.winfo_screenheight()
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    centro = '%dx%d+%d+%d' % (largura, altura, posx, posy)
    return centro