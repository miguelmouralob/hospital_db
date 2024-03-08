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
        doenças TEXT,
        email TEXT
    )
''')
connect.commit()

class Estados():
    def __init__(self):
        self.estados = ['AL', 'AP', 'AM', 'BA', 'CA', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 
                        'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

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

        sleep(1)
        while True:
            self.doenca = int(input('''Qual a doença classificada ao paciente?: 
    [0]AIDS
    [1]Alzheimer
    [2]AVC
    [3]Câncer
    [4]Covid
    [5]Dengue
    [6]Depressão
    [7]Diabetes
    [8]Hipertensão
    [9]Tuberculose\n
    Resposta: '''))
            
            match self.doenca:
                case 0:
                    self.doenca = 'AIDS'
                    break
                case 1:
                    self.doenca = 'Alzheimer'
                    break
                case 2:
                    self.doenca = 'AVC'
                    break
                case 3:
                    self.doenca = 'Câncer'
                    break
                case 4:
                    self.doenca = 'Covid'
                    break
                case 5:
                    self.doenca = 'Dengue'
                    break
                case 6:
                    self.doenca = 'Depressão'
                    break
                case 7:
                    self.doenca = 'Diabetes'
                    break
                case 8:
                    self.doenca = 'Hipertensão'
                    break
                case 9:
                    self.doenca = 'Tuberculose'
                    break
                case _:
                    sleep(1)
                    print('')
                    print('Escolha uma opção válida!')
                    print('')
                    sleep(1)


        cursor.execute('INSERT INTO pessoas (nome, idade, sexualidade, estado, faixa_etaria, doenças) VALUES (?, ?, ?, ?, ?, ?)', (self.n, self.idade, self.sexo, self.estado, self.faixaetaria, self.doenca))
        connect.commit()
        self.id = cursor.lastrowid

        self.email = f'{self.n.lower()}{self.id}{self.idade}@gmail.com'
        cursor.execute('UPDATE pessoas SET email = ? WHERE id = ?', (self.email, self.id))
        connect.commit()

class Pw():
    def __init__(self):
        sleep(1)
        print('')
        self.pw = int(input('Quer continuar? Sim(0) ou Não(1): '))


names = []

pw = -1

while pw != 1:
    pessoa = Nomes()
    print('')
    names.append(f'[{pessoa.id} - {pessoa.n} ({pessoa.idade}), {pessoa.sexo}, {pessoa.estado}, {pessoa.email}]')
    sleep(1)
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

    cursor.execute('SELECT nome, MIN(idade) FROM pessoas')
    result = cursor.fetchone()
    menornome_db, menoridade_db = result[0], result[1]

    cursor.execute('SELECT nome, MAX(idade) FROM pessoas')
    result = cursor.fetchone()
    maiornome_db, maioridade_db = result[0], result[1]

    cursor.execute('SELECT AVG(idade) FROM pessoas')
    media_bd = cursor.fetchone()[0]

connect.close()

sleep(1)
print(f'{maiornome_db} é a pessoa mais velha cadastrada no banco de dados gerada com {maioridade_db} anos. ')
sleep(1)
print(f'{menornome_db} é a pessoa mais nova cadastrada no banco de dados com {menoridade_db} anos. ')
sleep(1)
print('')
print(f'A média de idades cadastrada no banco de dados é de {media_bd:.2f} anos. ')
