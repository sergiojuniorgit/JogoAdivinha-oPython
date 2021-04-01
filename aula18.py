import random
import os


#variaveis
erros = 0
sorteado=random.randrange(0, 100)
jogador = int(input("Digite seu numero: "))


#inicio
while(sorteado != jogador):
    os.system('cls')
    if(sorteado > jogador):
        print("ERRO, numero é maior")
    elif(sorteado < jogador):
        print("Erro, numero é menor")
    erros += 1
    jogador=int(input("Digite seu número:"))
print("numero" + str(jogador)+", voce acertou em "+ str(erros + 1)+ " tentativas")