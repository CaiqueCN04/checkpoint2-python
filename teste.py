def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**(0.5))+1):
        if num % i == 0:
            return False
    return True

def primo_mais_proximo(num):
    menor = num - 1
    maior = num + 1
    while True:
        if eh_primo(menor):
            return menor
        elif eh_primo(maior):
            return maior
        menor -= 1
        maior += 1

while True:
    try:
        num = int(input("Digite um número entre 1 e 1000 (0 para sair): "))
        if num == 0:
            break
        elif num < 1 or num > 1000:
            print("Valor inválido. Digite novamente.")
            continue
        elif eh_primo(num):
            print(f"O número {num} é primo.")
            continue
        primo = primo_mais_proximo(num)
        print(f"O número primo mais próximo de {num} é {primo}.")
    except ValueError:
        print("Valor inválido. Digite novamente.")



