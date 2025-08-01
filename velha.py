matriz = [[0,0,0], [0,0,0], [0,0,0]]

count_x = 0
count_o = 0

while True:
    a = input('Digite a posição que você quer: ')
    b = input('Digite a posição que você quer: ')


    if a == b:
        print('Duas posições não podem!')
        break

    match a:
        case '1':
            matriz[0][0] = 'X'
        case '2':
            matriz[0][1] = 'X'
        case '3':
            matriz[0][2] = 'X'
        case '4':
            matriz[1][0] = 'X'
        case '5':
            matriz[1][1] = 'X'
        case '6':
            matriz[1][2] = 'X'
        case '7':
            matriz[2][0] = 'X'
        case '8':
            matriz[2][1] = 'X'
        case '9':
            matriz[2][2] = 'X'

    match b:
        case '1':
            matriz[0][0] = 'O'
        case '2':
            matriz[0][1] = 'O'
        case '3':
            matriz[0][2] = 'O'
        case '4':
            matriz[1][0] = 'O'
        case '5':
            matriz[1][1] = 'O'
        case '6':
            matriz[1][2] = 'O'
        case '7':
            matriz[2][0] = 'O'
        case '8':
            matriz[2][1] = 'O'
        case '9':
            matriz[2][2] = 'O'

    
    lista_x = ['X', 'X', 'X']
    lista_o = ['O', 'O', 'O']
    count = 0
    for i in matriz:
        print(f'{i[0]:<5} | {i[1]:^5} | {i[2]:>5}')
        count+=1
        if count == 1 or count == 2:
            print('-----------------------')
        if i == lista_x:
            print('O primeiro jogador ganhou')
            break
        if i == lista_o:
            print('O segundo jogador ganhou')
            break

    #Linha Vertical
    if matriz[0][0] == 'X' and matriz[1][0] == 'X' and matriz[2][0] == 'X':
        print('O primeiro jogador ganhou!') 
    if matriz[0][1] == 'X' and matriz[1][1] == 'X' and matriz[2][1] == 'X':
        print('O primeiro jogador ganhou!') 
    if matriz[0][2] == 'X' and matriz[1][2] == 'X' and matriz[2][2] == 'X':
        print('O primeiro jogador ganhou!')
        
    #Linha Diagonal
    if matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == 'X':
        print('O primeiro jogador ganhou')
    if matriz[0][2] == 'X' and matriz[1][1] == 'X' and matriz[2][0] == 'X':
        print('O primeiro jogador ganhou!')

    #Linha Vertical
    if matriz[0][0] == 'O' and matriz[1][0] == 'O' and matriz[2][0] == 'O':
        print('O segundo jogador ganhou!') 
    if matriz[0][1] == 'O' and matriz[1][1] == 'O' and matriz[2][1] == 'O':
        print('O segundo jogador ganhou!') 
    if matriz[0][2] == 'O' and matriz[1][2] == 'O' and matriz[2][2] == 'O':
        print('O segundo jogador ganhou!') 

    #Linha Diagonal
    if matriz[0][0] == 'O' and matriz[1][1] == 'O' and matriz[2][2] == 'O':
        print('O segundo jogador ganhou')
    if matriz[0][2] == 'O' and matriz[1][1] == 'O' and matriz[2][0] == 'O':
        print('O segundo jogador ganhou!')
        
    lista_sum = []
    for i in matriz:
        for j in i:
            lista_sum.append(j)
            
    if lista_sum.count('X') == 5 and lista_sum.count('O') == 4:
                print('Deu velha, otários!')
                break
    
