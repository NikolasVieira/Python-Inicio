from tkinter import *

root = Tk()
root.title("Avaliação - Pratica - 01") # Titulo da Janela.
root.geometry("600x500") # Resolução da Tela.
root["bg"] = "blue" # Cor de Fundo da Tela.

# FUNCTIONS
def executar():
    lblDados0['text'] = "Dados:"
    lblDados1['text'] = "Nome: "    +txtNome    .get()   
    lblDados2['text'] = "Cidade: "  +txtCidade  .get()
    lblDados3['text'] = "E-mail: "  +txtEmail   .get()
    lblDados4['text'] = "Telefone: "+txtTelefone.get()
    lblDados5['text'] = "Senha: *******"
    print(
        "Nome: "    +txtNome    .get()+",",
        "Cidade: "  +txtCidade  .get()+",",
        "E-mail: "  +txtEmail   .get()+",",
        "Telefone: "+txtTelefone.get()+",",
        "Senha: *******"
    )

# LABELS
lblTitulo   = Label(root,bg="white",fg="blue",font="arial 12 bold",text="AVALIAÇÃO DE PYTHON",width=60)
lblNome     = Label(root,bg="blue",fg="white",font="arial 11 bold",text="Nome:"    )
lblCidade   = Label(root,bg="blue",fg="white",font="arial 11 bold",text="Cidade:"  )
lblEmail    = Label(root,bg="blue",fg="white",font="arial 11 bold",text="E-mail:"  )
lblTelefone = Label(root,bg="blue",fg="white",font="arial 11 bold",text="Telefone:")
lblSenha    = Label(root,bg="blue",fg="white",font="arial 11 bold",text="Senha:"   )
lblDados0   = Label(root,bg="blue",fg="white",font="arial 11 bold")
lblDados1   = Label(root,bg="blue",fg="white",font="arial 11 bold")
lblDados2   = Label(root,bg="blue",fg="white",font="arial 11 bold")
lblDados3   = Label(root,bg="blue",fg="white",font="arial 11 bold")
lblDados4   = Label(root,bg="blue",fg="white",font="arial 11 bold")
lblDados5   = Label(root,bg="blue",fg="white",font="arial 11 bold")

# ENTRIES
txtNome     = Entry(root,bg="blue",width=80,highlightthickness=1)
txtCidade   = Entry(root,bg="blue",width=80,highlightthickness=1)
txtEmail    = Entry(root,bg="blue",width=80,highlightthickness=1)
txtTelefone = Entry(root,bg="blue",width=80,highlightthickness=1)
txtSenha    = Entry(root,bg="blue",width=80,highlightthickness=1)

# BUTTONS
btnSalvar = Button(root,text="Salvar",bg="yellow",fg="blue",width=10,height=2,font="arial 12 bold",command=executar)

# LAYOUTS
# titulo
lblTitulo.grid(columnspan=3,sticky="we")

lblNome    .grid(row=1,column=0,pady=10,sticky=W)
lblCidade  .grid(row=2,column=0,pady=10,sticky=W)
lblEmail   .grid(row=3,column=0,pady=10,sticky=W)
lblTelefone.grid(row=4,column=0,pady=10,sticky=W)
lblSenha   .grid(row=5,column=0,pady=10,sticky=W)

txtNome    .grid(row=1,column=1)
txtCidade  .grid(row=2,column=1)
txtEmail   .grid(row=3,column=1)
txtTelefone.grid(row=4,column=1)
txtSenha   .grid(row=5,column=1)

btnSalvar.grid(row=6,columnspan=3,pady=10)

lblDados0.grid(row=7,column=0,sticky=W)
lblDados1.grid(row=7,column=1,sticky=W)
lblDados2.grid(column=1,sticky=W)
lblDados3.grid(column=1,sticky=W)
lblDados4.grid(column=1,sticky=W)
lblDados5.grid(column=1,sticky=W)


root.mainloop() # Executa a Tela.