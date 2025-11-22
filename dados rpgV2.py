from random import randint

def dados_lados (lados):
    return randint (1,lados)

def jogar_dado ():
    print ('Rolando dado...')


    
    
dadodvinte = dados_lados(20)
print (f'O valor do dado D20 é: {dadodvinte}')
if dadodvinte == 20:
    print ('Você acertou um crítico!')

if dadodvinte == 20:
    dadodcem = dados_lados(100)
    print (f'O valor do dado D100 é: {dadodcem}')
    if 100 >= dadodcem > 95:
        print ('Você passou!')
        exit()
    
    elif 94 > dadodcem > 90:
        print ('Chute um valor para um dado D4 e jogue o dado, caso caia o número chutado, você acertará o FF, caso o contrário, o progresso será salvo e o próximo crítico voltará desse estado.')
        
        try:
            chute_d4 = int(input('Digite o valor para o chute do dado D4 (1-4)'))
            if not 1 <= chute_d4 <= 4:
                print ('Número inválido, digite um valor de 1 a 4')
                
        except ValueError:
            print ('Entrada inválida, digite um número inteiro')
            
        
        dadodquatro = dados_lados(4)
        print (f'O valor do dado D4 é {dadodquatro}')
        
        if dadodquatro == chute_d4:
            print ('O FF foi acertado.')
        
        else:
            print ('O FF não foi acertado, o progresso do crítico será salvo.')
    else:
        print ('A verificação do D100 falhou')
        
else:
    print ('Não foi acertado o crítico no D20')
    
print('Fim da rodada de dados')
                           
                           
