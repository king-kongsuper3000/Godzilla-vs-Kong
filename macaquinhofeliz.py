import random
numero_secreto = round(random.uniform(1, 100), 2)
tentativas = 0
max_tentativas = 15

# --- ADIÇÃO 1: Ranking de recorde ---
recorde = 15 

while tentativas < max_tentativas:
    # --- ADIÇÃO 2: Tratamento de erro (try/except) ---
    try:
        entrada = input("tente adivinhar o numero que estou pensando (1-100): ")
        palpite = float(entrada)
    except ValueError:
        print("Ops! Digite um número válido (ex: 50.5).")
        continue

    tentativas += 1
    
    # --- ADIÇÃO 3: Sistema de proximidade (Dica extra) ---
    distancia = abs(palpite - numero_secreto)
    if distancia <= 5 and palpite != numero_secreto:
        print("Você está MUITO perto!")
    elif distancia > 20:
        print("Está meio frio por aqui...")

    if palpite < numero_secreto:
        print("quase la! tente um numero maior")
    elif palpite > numero_secreto:
        print("quase la! tente um numero menor")
    elif palpite == numero_secreto:
        print(f"parabens! você acertou o numero em {tentativas} tentativas")
        # --- ADIÇÃO 4: Feedback de performance ---
        if tentativas < recorde:
            print("Novo Recorde Pessoal!")
        break

    if tentativas == max_tentativas:
        print("infelizmente, você não acertou. o numero era", numero_secreto)
        print("fim de jogo!")
        break
    else:
        print(f"você tem {max_tentativas - tentativas} tentativas restantes")
