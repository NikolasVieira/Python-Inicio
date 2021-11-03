from tkinter import *

menu = Tk()
menu.title("Iniciando no Python Tkinter") # Titulo da Janela.
menu.geometry("600x400") # Resolução da Tela.
menu["bg"] = "purple" # Cor de Fundo da Tela.

btnOk = Button(menu,text="Me Aperte",width=10,height=4,bg="cyan",fg="red",font="Arial 15") # Define um Botão
btnOk.pack() # Cria o Botão Definido

menu.mainloop() # Executa a Tela.