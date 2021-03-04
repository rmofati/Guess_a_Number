import random
#import functions

max_number = 1000

def tentativa(number):
    terminou = False
    guess = input(f"Escreva um número entre 0 e {max_number}: ")
    guess = int(guess)
    
    while terminou != True:
        if guess >= 0 and guess <= max_number:
            if int(guess) == number:
                print("Parabéns! Você conseguiu encontrar o número que eu pensei!")
                terminou = True
            elif guess < number:
                print(f"O número {guess} é menor do que o número que eu escolhi. Tente novemente")
                tentativa(number)
            elif guess > number:
                print(f"O número {guess} é maior do que o número que eu escolhi. Tente novemente")
                tentativa(number)
        else:
            print("Valores não permitidos. Tente novamente")
            break

print("Olá! Seja bem-vindo ao Guess a Number.")
print(f"Eu irei escolher um número entre 0 e {max_number} e você deverá achar qual é esse número. Está preparado?")

answer = input("Pronto para continuar? [Sim/Não] ")

while answer.lower() != "sim" or answer.lower() != "não" or answer.lower() != "s" or answer.lower() != "n":
    if answer.lower() == "sim" or answer.lower() == "s":
        number = random.randint(0,1000)
        print("Pronto! Já escolhi o número. Agora é com você!")
        tentativa(number)
    elif answer.lower() == "não" or answer.lower() == "n":
        print("Tchau!")
        break
    else:
        print("Opa! Parece que você não digitou a resposta corretamente. Digite somente Sim ou Não")
        answer = input("Pronto para continuar? [Digite Sim ou Não] ")