boletim = list()

lista1 = list()
lista2 = list()
lista3 = list()

while True:
    nome = str(input('Insira o nome do aluno: '))
    n1 = float(input('Insira a primeira nota: '))
    n2 = float(input('Insira a segunda nota: '))
    n3 = float(input('Insira a terceira nota: '))
    media = (n1 + n2 + n3)/3
    
    boletim.append([nome, ['NOTA 1', n1], ['NOTA 2', n2], ['NOTA 3',n3], media])
    
    if media >=7:
        print('Situação: APROVADO')
    else: ('Situação: REPROVADO')
    print('==' * 40)
    
    proximo = str(input('Registrar próximo aluno? [S/N]'))
    print('=='* 40)
    if proximo in "Nn":
        print('\n', boletim)
        print('==' * 40)
    
    finalizar = str(input('Deseja finalizar? [S/N]'))
    print('=='* 40)

    if finalizar in 'Ss':
        break
