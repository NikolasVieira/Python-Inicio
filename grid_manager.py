from tkinter import *

def btnExecutar_Click():
    print("Informações Recebidas")

root = Tk()
root.title("Grid - Manager") # Titulo da Janela.
root.geometry("600x400") # Resolução da Tela.
root["bg"] = "purple" # Cor de Fundo da Tela.

# Define as Labels
lblNome   = Label(root,text="Nome:"  ).grid()
lblCidade = Label(root,text="Cidade:").grid()
lblEmail  = Label(root,text="E-mail:").grid()

# Define Caixas de Texto
txtNome   = Entry(root).grid(row=0, column=1)
txtCidade = Entry(root).grid(row=1, column=1)
txtEmail  = Entry(root).grid(row=2, column=1)

# Define o Botão
btnExecutar = Button(root,text="Enviar",bg="green",width=15,height=4,fg="yellow", command=lambda:btnExecutar_Click())
btnExecutar.grid(row=3, column=1)

root.mainloop() # Executa a Tela.