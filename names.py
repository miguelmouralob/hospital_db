class Nomes():
    def __init__(self):
        self.n = input('Digite seu nome: ').title()
        self.id = int(input('Digite sua idade: '))

class Pw():
    def __init__(self):
        self.pw = int(input('Quer continuar? Sim(0) ou Não(1): '))

names = []
maioridade = 0
maiornome = ''

pw = -1

while pw != 1:
    pessoa = Nomes()
    names.append(f'[{pessoa.n} ({pessoa.id})]')
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
        maioridade = pessoa.id
        maiornome = pessoa.n

print(f'{maiornome} é a pessoa mais velha do grupo com {maioridade} anos. ')
