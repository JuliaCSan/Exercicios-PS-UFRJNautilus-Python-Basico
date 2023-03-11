boletim = list()
while True:
    nome = str(input('Insira o nome do aluno: '))
    n1 = float(input('Insina a primeira nota: '))
    n2 = float(input('Insira a segunda nota: '))
    n3 = float(input('Insira a terceira nota: '))
    media = (n1 +n2 +n3)/3
    print('Média: ', media)
    boletim.append([nome, [n1, n2, n3], media])

    if media >=7:
        print('Situação: APROVADO')
    else: print('Situação: REPROVADO')
        
    proximo = str(input('Deseja cadastrar o próximo aluno? [S/N]'))
    if proximo in 'Nn':
        break
        
print('-=' * 40)
print(f'{"NOME":<4}{"NOTA 1":<12}{"NOTA 2":<15}{"NOTA 3":<18}{"MÉDIA":<22}')
for i in enumerate[boletim]:
    print(f'{nome:<4}{n1:<12}{n2:<15}{n3:<18}{media:<22}')
    


    

    
    
        

