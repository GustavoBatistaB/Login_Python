import sqlite3

conn = sqlite3.connect('Usuarios.db')

cursor = conn.cursor()

#criando a tabela 

cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuario (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Senha TEXT NOT NULL,
    Telefone TEXT NOT NULL
);            
""")
print("BD")

    
#NOME< SENHA  TELEFONE 
