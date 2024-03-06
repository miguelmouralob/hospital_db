import sqlite3

connect = sqlite3.connect('dados_pessoas.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        sexualidade TEXT,
        email TEXT
    )
''')
connect.commit()

class Nomes():
    def __init__(self): 
        self.n = input('Digite o nome do usuário: ').title()

        while True:
            self.idade = int(input('Digite a idade: '))
            if self.idade >= 18 and self.idade <= 70:
                break
            else:
                print('Apenas pesseoas entre 18-70 anos são aceitas!')

        while True:
            self.sexo = input('Digite a sexualidade (Masculino(M) OU Feminino(F)): ').upper()
            if self.sexo.startswith('M') or self.sexo.startswith('F'):
                break
            else:
                print('É preciso escolher o genêro entre Masculino(M) e Feminino(F)!')

        self.email = f'{self.n.lower()}{self.idade}@gmail.com'
        cursor.execute('INSERT INTO pessoas (nome, idade, sexualidade, email) VALUES (?, ?, ?, ?)', (self.n, self.idade, self.sexo, self.email))
        connect.commit()
        self.id = cursor.lastrowid 

class Pw():
    def __init__(self):
        self.pw = int(input('Quer continuar? Sim(0) ou Não(1): '))


#class Sex():
#    if pessoa.sexo == 


names = []
maioridade = 0
maiornome = ''

pw = -1

while pw != 1:
    pessoa = Nomes()
    names.append(f'[{pessoa.id} - {pessoa.n} ({pessoa.idade}), {pessoa.sexo}, {pessoa.email}]')
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

    if pessoa.idade > maioridade:
        maioridade = pessoa.idade
        maiornome = pessoa.n

connect.close()

print(f'{maiornome} é a pessoa mais velha do grupo com {maioridade} anos. ')
