import random
vidas = int(input("Digite a quantidade de vidas: "))
balas = int(input("Digite o numero de balas que voce quer roletar: "))


def funcao_esperar():
    from time import sleep
    for _ in range(3):
        print(".")
        sleep(0.5)
    print("Preparar...\nApontar...\n...")
    
def roleta(vida,balas):
    if(balas <= 6 and balas > 0):
        print("Iniciando o jogo!")
        funcao_esperar()
        for i in range(vidas):
            chance = 1/balas
            for j in range(balas):
                roleta = random.binomialvariate(balas, chance)
                if(roleta == 0):
                    funcao_esperar()
                    print('Você morreu na primeira bala, com a {} vida'.format(i+1))
                    break
                if(roleta > 0 and chance !=0):
                    if(1/(balas-1) == 0):
                            print('Você morreu na {}'.format(balas)) 
                    chance = 1/(balas-1)
                    roleta = random.binomialvariate(balas, chance)
                    if(roleta == 0):
                        funcao_esperar()
                        print('Você morreu na segunda bala, com a {} vida'.format(i+1))
                        break
                    if(roleta > 0 and chance!=0):
                        if(1/(balas-1) == 0):
                            print('Você morreu na {}'.format(balas))  
                        chance = 1/(balas-1)
                        roleta = random.binomialvariate(balas, chance)
                        if(roleta == 0):
                            print('Você morreu na terceira bala, com a {} vida'.format(i+1))
                            break
                        if(roleta > 0 and chance!=0):
                            if(1/(balas-1) == 0):
                                funcao_esperar()
                                print('Você morreu na {}'.format(balas)) 
                            chance = 1/(balas-1)
                            roleta = random.binomialvariate(balas, chance)
                            if(roleta == 0):
                                funcao_esperar()
                                print('Você morreu na quarta bala, com a {} vida'.format(i+1))
                                break
                            if(roleta > 0 and chance!=0):
                                if(1/(balas-1) == 0):
                                    funcao_esperar()
                                    print('Você morreu na {}'.format(balas)) 
                                chance = 1/(balas-1)
                                roleta = random.binomialvariate(balas, chance)
                                if(roleta == 0):
                                    funcao_esperar()
                                    print('Você morreu na quinta bala, com a {} vida'.format(i+1))
                                    break
                                if(roleta > 0 and chance!=0):
                                    if(1/(balas-1) == 0):
                                        funcao_esperar()
                                        print('Você morreu na {}'.format(balas)) 
                                    roleta = random.binomialvariate(balas, chance)
                                    if(roleta == 0 and chance == 1):
                                        funcao_esperar()
                                        print('Você morreu na sexta bala, com a {} vida'.format(i+1))
                                        break
                                    else:
                                        print("Fodase voce morreu nao sei como mas nao morreu, parabens pena que agora voce vai morrer de velhice")
                                        break
    else:
        print('Balas insuficientes')                            
                

roleta(vidas, balas)


