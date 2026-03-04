import random
numero_secreto =round(random.uniform(1, 100), 2)
tentativas = 0
max_tentativas = 15

while tentativas < max_tentativas:
    palpite = float(input("tente adivinhar o numero que estou pensando, entre 1 e 100: "))
    tentativas += 1
    if palpite < numero_secreto:
        print("quase la! tente um numero maior")
    elif palpite > numero_secreto:
        print("quase la! tente um numero menor")
    elif palpite == numero_secreto:
        print(f"parabens! você acertou o numero em {tentativas} tentativas")
        break

    if tentativas==max_tentativas:
        print("infelizmente, você não acertou. o numero era", numero_secreto)
        print("fim de jogo!")
        break
    else:
        print( f"você tem {max_tentativas - tentativas} tentativas restantes")
