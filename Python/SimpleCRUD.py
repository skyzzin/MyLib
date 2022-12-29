
import sqlite3

def PrintDB():
     banco = sqlite3.connect('banco.db')
     cursor = banco.cursor()
     cursor.execute("SELECT * FROM users")
     for linha in cursor.fetchall():
        print(linha)

        
def InsertDB(nome,senha):
    banco = sqlite3.connect('banco.db')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(nome VARCHAR,senha INT)')
    nome= nome
    senha= senha
    cursor.execute("INSERT INTO users(nome,senha) VALUES(?,?) ",(nome,senha))
    cursor.execute("SELECT * FROM users")
    for linha in cursor.fetchall():
        print(linha)
    banco.commit()
    banco.close()

def SearchDB(nome,senha):
    banco = sqlite3.connect('banco.db')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(nome VARCHAR,senha INT)')
    nome = nome  
    senha = senha
    cursor.execute("SELECT * FROM users WHERE nome=? AND senha=? ",(nome,senha))
    for linha in cursor.fetchall():
        print(linha)
    banco.commit()
    banco.close()

