from tkinter import  Tk, Entry,Label,Scrollbar,Text,Button,Listbox,Toplevel
import tkinter
import pandas as pd
import os


def frame():
    return pd.read_csv('Minha Lista.csv')
dados_enviar = lambda x,y: {'TÍTULO':x,'DESCRIÇÃO':y}

def criando():
    dados = dados_enviar(titulo.get(),descricao.get(1.0,50000.0).replace('\n','.'))
    frame = pd.DataFrame([dados])
    frame.to_csv('Minha Lista.csv',index=False)

def atualizando():
    data_frame = frame()
    dados = dados_enviar(titulo.get(),descricao.get(1.0,50000.0).replace('\n','.'))
    data_frame.loc[len(data_frame) +1] = dados
    data_frame.to_csv('Minha Lista.csv',index=False)

def deletando():
    data_frame = frame()
    data_frame.drop()

def inserindo_dados():
    verificando_dados = os.listdir()
    if 'Minha Lista.csv' in verificando_dados:
        atualizando()
    else:
        criando()

def retornando():
    lista.destroy
    #ler os dados da planilha
    frame = pd.read_csv('Minha Lista.csv')
    #pegar a coluna titulo e seu indice e formatar texto

    for i,item in enumerate(frame['TÍTULO']):
        lista.insert(tkinter.END,f'{i} - {item}')


def lendo_lista(lendo):
    item_ativo = lista.curselection()
    data_frame = frame()
    indice_selecionado = data_frame.loc[item_ativo[0]]

    descricao_da_pagina = Toplevel(win)
    descricao_da_pagina.title(indice_selecionado[0])
    descricao_do_item = Label(descricao_da_pagina,text=indice_selecionado[1].replace('.','\n'))
    descricao_do_item.pack()
    descricao_da_pagina.geometry("300x200")

win = Tk()
win.title('TO-DO List')
#campo de titulo
label_titulo = Label(win,text='Título',font=(50),width=10)
titulo = Entry()
#campo de descrição
label_descricao = Label(win, text='Descrição',font=(50))
descricao = Text(win, height=10, width=30)
#botão de envio
bt_enviar = Button(text='Enviar', width=20, command=inserindo_dados)

lista = Listbox(win)
lista.bind('<<ListboxSelect>>', lendo_lista)
label_titulo.pack()
titulo.pack()
label_descricao.pack()
descricao.pack()
bt_enviar.pack(pady=10)
lista.pack(pady=10)



retornando()


win.geometry('350x350')
win.mainloop()