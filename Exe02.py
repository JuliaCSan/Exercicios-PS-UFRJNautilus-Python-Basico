boletim = list()
lista_notas1 = list()
lista_notas2 = list()
lista_notas3 = list()

while True:
    nome = str(input('\nInsira o nome do aluno: '))
    n1 = float(input('Insina a primeira nota: '))
    n2 = float(input('Insira a segunda nota: '))
    n3 = float(input('Insira a terceira nota: '))
    media = (n1 +n2 +n3)/3

    print('Média: ', media)

    boletim.append([nome, ['NOTA 1:'], n1, ['NOTA 2: ', n2], ['NOTA 3 :', n3], media])
    lista_notas1.append(n1)
    lista_notas2.append(n2)
    lista_notas3.append(n3)

    if media >=7:
        print('Situação: APROVADO')
    else: print('Situação: REPROVADO')

    proximo = str(input('\nDeseja cadastrar o próximo aluno? [S/N]'))
    if proximo in 'Nn':
        print ('=' * 40)
        print(boletim)
        print ('=' * 40)
        print('AV1: ', lista_notas1)
        print('AV2: ', lista_notas2)
        print('AV3: ', lista_notas3)
        print ('=' * 40)
    


    

    
    
        

