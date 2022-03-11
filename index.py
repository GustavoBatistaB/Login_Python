# importando as bibliotecas 
from atexit import register
from tkinter import *
from tkinter import messagebox
from turtle import left, right
from tkinter import ttk
import database

# Criando janela 

janela = Tk()
janela.title("DS Sistema de Login ")
janela.geometry("600x300")
janela.config(background="white")
janela.resizable(width=False, height= False)
janela.attributes("-alpha", 0.9)
# carregando logo
logo = PhotoImage(file="imagens/logo.png")
# Adicionando o Icon 
janela.iconbitmap(default="imagens/logoicon.ico")


# Dividindo a janela em dois 

LeftFrame = Frame(janela, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)
RightFrame = Frame(janela, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side= RIGHT)

# Adicionando a logo 
LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50,y=100)

# adicionandno 

UserLabel = Label(RightFrame, text="Nome do Usuario:",font=("ariel", 15), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=53)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=180, y=57)

PassLabel = Label(RightFrame,text="Senha: ", font=("ariel",15), bg="MIDNIGHTBLUE", fg="white" )
PassLabel.place(x=5, y= 80)

PassEntry= ttk.Entry(RightFrame, width=45, show="*")
PassEntry.place(x=90, y=85 )

def Login():
    Nome = UserEntry.get()
    Senha = PassEntry.get()    
    
    database.cursor.execute("""
    SELECT * FROM Usuario                        
    WHERE (Nome = ? AND Senha = ?)
    """, (Nome, Senha))
    verifyLogin = database.cursor.fetchone()
    try:
        if (Nome in verifyLogin and Senha in verifyLogin ):
            messagebox.showinfo(title="Acesso", message="Bem Vindo (a) ")
    except:
        messagebox.showinfo(title="Acesso", message="Acesso negado ")    

LoginButton = ttk.Button(RightFrame, text = "Login", width=10, command=Login)
LoginButton.place(x=90, y= 200)

def Registrar ():
    # Removendo os botões 
    LoginButton.place(x=10000,y=10000)
    RegisterButton.place(x=10000,y=10000)
    # Inserindo 
    TelLabel = Label(RightFrame, text="Telefone:",font=("ariel",15), bg="MIDNIGHTBLUE",fg="white")
    TelLabel.place(x=5,y=110)
    
    TelEntry = ttk.Entry(RightFrame,width=45)
    TelEntry.place(x=90,y=115)
    
    EmailLabel = Label(RightFrame,text="E-mail:",font=("ariel",15), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5,y=140)
    
    EmailEntry = ttk.Entry(RightFrame,width=45)
    EmailEntry.place(x=90, y=145)
    
    
    def RegisterToDataBaser():
        Nome = UserEntry.get()
        Email =  EmailEntry.get()
        Senha = PassEntry.get()
        Telefone = TelEntry.get()
        
        if (Nome == "" and Email == "" and  Senha == "" and Telefone == ""):
            messagebox.showerror(title="Erro no Registro", message="Preencha todos os campos ")
        else:
            
            database.cursor.execute(""" 
            INSERT INTO Usuario(Nome,Email,Senha,Telefone) VALUES(?,?,?,?)
            """,(Nome,Email, Senha, Telefone))
            database.conn.commit()
            messagebox.showinfo(title="Informação de registro", message="Conta criada com sucesso")
            
    
    
    
    # Inserindo os botões 
    Registrar = ttk.Button(RightFrame, text="Registrar",width=20, command=RegisterToDataBaser)
    Registrar.place(x=200,y=200)
    
    def BackToLogin ():
        TelLabel.place(x=10000)
        TelEntry.place(x=10000)
        EmailLabel.place(x=10000)
        EmailEntry.place(x=10000)
        BackButton.place(x=10000)
        LoginButton.place(x=90, y= 200)
        Registrar.place(x=10000)
        RegisterButton.place(x=200, y=200)
        
        
        
    BackButton = ttk.Button(RightFrame, text="Voltar",width=15, command=BackToLogin)
    BackButton.place(x=90,y=200)
    
    

RegisterButton = ttk.Button(RightFrame, text="Registrar",width=20, command=Registrar)
RegisterButton.place(x=200, y=200)




janela.mainloop()