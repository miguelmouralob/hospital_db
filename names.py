import sqlite3

connect = sqlite3.connect('dados_pessoas.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER
    )
''')
connect.commit()




class Nomes():
    def __init__(self):
        self.n = input('Digite o nome do usuário: ').title()
        self.idade = int(input('Digite a idade: '))
        cursor.execute('INSERT INTO pessoas (nome, idade) VALUES (?, ?)', (self.n, self.idade))
        connect.commit()
        self.id = cursor.lastrowid

class Pw():
    def __init__(self):
        self.pw = int(input('Quer continuar? Sim(0) ou Não(1): '))

names = []
maioridade = 0
maiornome = ''

pw = -1

while pw != 1:
    pessoa = Nomes()
    names.append(f'[{pessoa.id} - {pessoa.n} ({pessoa.idade})]')
    print(', '.join(names))

    kp = -1

    while kp != 1:
        continuar = Pw()

        match continuar.pw:
            case 0:
                kp = 1
                break
            case 1:
                pw = 1
                print('')
                break
            case _:
                print('Digite uma opção válida!')

    if pessoa.id > maioridade:
        maioridade = pessoa.idade
        maiornome = pessoa.n

connect.close()

print(f'{maiornome} é a pessoa mais velha do grupo com {maioridade} anos. ')
