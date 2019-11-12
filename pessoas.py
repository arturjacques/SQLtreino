from cores import letraAma,letraAzu,letraNor,letraVer
import sqlite3

pessoas=[]
pathdb='db\estudo.db'
nome_tabela='pessoas'

#Conectando ao banco de dados ou criando e conectando
conn = sqlite3.connect(pathdb)

#Definindo cursor
cursor = conn.cursor()

try:

    cursor.execute(f"""
SELECT * FROM {nome_tabela};
""")

except:
    cursor.execute(f"""
    CREATE TABLE {nome_tabela}(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade Integer
    );
    """)

#Fechando banco de dados
conn.close()


while True:
    print(f'{letraNor()}{"-"*40}')
    print(f'{"MENU PRINCIPAL":^40}')
    print('-'*40)
    print(f'''{letraAma()}1 -{letraAzu()} Ver pessoas cadastradas
{letraAma()}2 -{letraAzu()} Cadastrar nova Pessoa
{letraAma()}3 -{letraAzu()} Sair do Sistema''')
    print(f'{letraNor()}{"-"*40}')
    while True:
        a = input(f'{letraAma()}Sua Opção:')
        if a not in '123':
            print(f'{letraVer()} Erro. Número invalido')
        else:
            a=int(a)
            break
    #Ver pessoas cadastradas
    if a==1:
        print(f'{letraAma()}',end='')
        print('-'*40)
        print(f'{letraVer()}{"Pessoas Cadastradas":^40}{letraAma()}')
        print('-'*40)
        print(f'{letraNor()}', end='')
        print(f'{"Nome":<30}{"Idade":<10}')
        conn = sqlite3.connect(pathdb)
        cursor = conn.cursor()
        cursor.execute(f"""
        SELECT * FROM {nome_tabela};
        """)
        for i in cursor.fetchall():
            print(f'{i[1]:<30}{i[2]:<3}Anos')
        conn.close()
    #Cadastrar Pessoas
    elif a==2:
        pessoas.append(input('Digite o nome: ').strip().title())
        pessoas.append(input('Digite a idade: '))
        conn = sqlite3.connect(pathdb)
        cursor = conn.cursor()
        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO pessoas (nome, idade)
        VALUES (?,?)
        """, (pessoas[0], pessoas[1]))
        conn.commit()
        pessoas.clear()
    elif a==3:
        break

