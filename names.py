import sqlite3
from time import sleep

connect = sqlite3.connect('dados_pessoas.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        sexualidade TEXT,
        estado TEXT,
        faixa_etaria TEXT,
        email TEXT
    )
''')
connect.commit()

class Estados():
    def __init__(self):
        self.estados = ['AL', 'AP', 'AM', 'BA', 'CA', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

selecionar = Estados()

class Nomes():
    def __init__(self): 
        self.n = input('Digite o nome do usuário: ').title()
        sleep(1)

        while True:
            self.idade = int(input('Digite a idade: '))
            sleep(1)
            if self.idade >= 16 and self.idade <= 70:
                break
            else:
                print('Apenas pesseoas entre 16-70 anos são aceitas!')

        if 16<= self.idade <= 19:
            self.faixaetaria = 'Jovem'
        elif 20<= self.idade <= 59:
            self.faixaetaria = 'Adulto'
        elif 60<= self.idade <= 70:
            self.faixaetaria = 'Idoso'
        else:
            print('Apenas pesseoas entre 16-70 anos são aceitas!')


        while True:
            self.sexo = input('Digite a sexualidade (Masculino(M) OU Feminino(F)): ').upper()
            sleep(1)
            if self.sexo.startswith('M') or self.sexo.startswith('F'):
                break
            else:
                print('É preciso escolher o genêro entre Masculino(M) e Feminino(F)!')

        while True:
            self.estado = input('Digite o estado: ').upper()
            sleep(1)
            if self.estado in selecionar.estados:
                break
            else:
                print('Digite a sigla de um estado existente!')

        cursor.execute('INSERT INTO pessoas (nome, idade, sexualidade, estado, faixa_etaria) VALUES (?, ?, ?, ?, ?)', (self.n, self.idade, self.sexo, self.estado, self.faixaetaria))
        connect.commit()
        self.id = cursor.lastrowid

        self.email = f'{self.n.lower()}{self.id}{self.idade}@gmail.com'
        cursor.execute('UPDATE pessoas SET email = ? WHERE id = ?', (self.email, self.id))
        connect.commit()

class Pw():
    def __init__(self):
        sleep(1)
        self.pw = int(input('Quer continuar? Sim(0) ou Não(1): '))


names = []
medidade = []

menoridade = 70
maioridade = 0
menornome = ''
maiornome = ''

pw = -1

while pw != 1:
    pessoa = Nomes()
    names.append(f'[{pessoa.id} - {pessoa.n} ({pessoa.idade}), {pessoa.sexo}, {pessoa.estado}, {pessoa.email}]')
    sleep(1)
    print(', '.join(names))

    medidade.append(pessoa.idade)

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

    if pessoa.idade < menoridade:
        menoridade = pessoa.idade
        menornome = pessoa.n


    cursor.execute('SELECT idade FROM pessoas')
    idades_bd = cursor.fetchall()

    idades_bd = [age[0] for age in idades_bd]

    media_bd = sum(idades_bd) / len(idades_bd)


connect.close()

sleep(1)
print(f'{maiornome} é a pessoa mais velha dentro dessa lista gerada com {maioridade} anos. ')
sleep(1)
print(f'{menornome} é a pessoa mais nova dentro dessa lista gerada com {menoridade} anos. ')
sleep(1)
print('')
print(f'A média de idades no banco de dados é de {media_bd} anos. ')
