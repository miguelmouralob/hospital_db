import sqlite3

connect = sqlite3.connect('dados_pessoas.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        sexualidade TEXT,
        estado TEXT,
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

        while True:
            self.estado = input('Digite o estado: ').upper()
            if self.estado in selecionar.estados:
                break
            else:
                print('Digite a sigla de um estado existente!')

        cursor.execute('INSERT INTO pessoas (nome, idade, sexualidade, estado) VALUES (?, ?, ?, ?)', (self.n, self.idade, self.sexo, self.estado))
        connect.commit()
        self.id = cursor.lastrowid

        self.email = f'{self.n.lower()}{self.id}{self.idade}@gmail.com'
        cursor.execute('UPDATE pessoas SET email = ? WHERE id = ?', (self.email, self.id))
        connect.commit()

class Pw():
    def __init__(self):
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

    
    media = sum(medidade) / len(medidade)

connect.close()

print(f'{maiornome} é a pessoa mais velha dentro dessa lista gerada com {maioridade} anos. ')
print(f'{menornome} é a pessoa mais nova dentro dessa lista gerada com {menoridade} anos. ')
print('')
print(f'A média de idades nessa lista é de {media} anos. ')
