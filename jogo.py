import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("=== JOGO DE ADVINHA ===")
print("Escolhi um numero entre 1 e 100!")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f" Acertou em {tentativas} tentativas!")
        break
    elif palpite < numero_secreto:
        print("Maior!")
    else:
        print("Menor!")