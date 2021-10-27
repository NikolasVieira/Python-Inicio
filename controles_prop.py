from tkinter import *

menu = Tk()
menu.title("Controles - Propriedades") # Titulo da Janela.
menu.geometry("600x400") # Resolução da Tela.
menu["bg"] = "cyan" # Cor de Fundo da Tela.

lblNome = Label(menu,text="Sou uma Label",width=15,height=4,bg="purple",fg="yellow",font="Arial 15",bd=2,relief="solid") # Define uma Label
lblNome.pack() # Cria a Label Definida

btnExibir = Button(menu,text="Clique em Mim",width=15,height=4,bg="purple",fg="yellow",font="Arial 15",command=lambda:btnExibir_Click("Buuuu!!!")) # Define uma Botão que Envia uma Mensagem no Terminal
btnExibir.pack() # Cria o Botão Definido

def btnExibir_Click(mensagem):print(mensagem)

txtNome = Entry(menu).pack() # Cria um Campo de Texto

menu.mainloop() # Executa a Tela.