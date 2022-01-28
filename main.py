from tkinter import *
from tkinter import ttk
import datetime

lista_tipos = ['Galao', 'Caixa', 'Saco', 'Unidade']
codigos = []
janela = Tk()
janela.title('Interface Grafica de Produtos')


def inserir():
    desc = entrada.get()
    tipo = combobox.get()
    qtd = qtdUnidade.get()
    data = datetime.datetime.now()
    data = data.strftime('%d/%m/%y %H:%M')
    codigo = len(codigos) + 1
    codigos.append((codigo, desc, tipo, qtd, data))


def exibir():
    texto['text'] = codigos


desc = Label(janela, text='Descrição Materiais')
desc.grid(column=0, row=0, padx=20, pady=10, sticky='nswe', columnspan=4)

entrada = Entry(janela)
entrada.grid(column=0, row=1, padx=20, pady=10, sticky='nswe', columnspan=4)

unidade = Label(janela, text='Tipo da Unidade do Materia:')
unidade.grid(column=0, row=2, padx=20, pady=10, sticky='nswe', columnspan=2)

combobox = ttk.Combobox(values=lista_tipos)
combobox.grid(column=2, row=2, padx=20, pady=10, sticky='nswe', columnspan=2)

qtd = Label(janela, text='Quantida de UND de Material')
qtd.grid(column=0, row=3, pady=10, padx=20, sticky='nswe', columnspan=2)

qtdUnidade = Entry(janela)
qtdUnidade.grid(column=2, row=3, pady=10, padx=20, sticky='nswe', columnspan=2)

botao = Button(janela, text='Criar', command=inserir)
botao.grid(column=0, row=4, pady=10, padx=20, sticky='nswe', columnspan=2)

botao_exibir = Button(janela, text='exibir', command=exibir)
botao_exibir.grid(column=2, row=4, pady=10, padx=20, sticky='nswe', columnspan=2)

texto = Label(janela, text="")
texto.grid(column=0, row=5, pady=10, padx=20, sticky='nswe', columnspan=4)

janela.mainloop()
