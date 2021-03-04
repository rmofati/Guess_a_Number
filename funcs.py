def presentation():
    print("")
    print("+=======================================+")
    print("|     Hi! Welcome to Guess a Number     |")
    print("| Olá! Seja bem-vindo ao Guess a Number |")
    print("+=======================================+")
    print("")
    
def language():
    print("+================================+")
    print("|      Choose your language      |")
    print("|        Escolha a língua        |")
    print("|  [1] Português / [2] English   |")
    print("+================================+")
    
    language = input("->: ")
    
    while language != "1" or language != "2":
        if language == "1":
            language = "PT-BR"
            return language
        elif language == "2":
            language = "EN"
            return language
        else:
            print("This answer is incorrect. Choose 1 or 2")
            print("Esta resposta não é possível. Escolha somente 1 ou 2")
            language = input("->: ")

def tentativa(number, max_number, language):
    if language == "PT-BR":
        print("")
        guess = input(f"Escreva um número entre 0 e {max_number}: ")
        guess = int(guess)
        
        if guess >= 0 and guess <= max_number:
            if int(guess) == number:
                print("")
                print("+==================================================+")
                print("|                    PARABÉNS!                     |")
                print("| Você conseguiu encontrar o número que eu pensei! |")
                print("+==================================================+")
                return True
            elif guess < number:
                print(f"O número {guess} é menor do que o número que eu escolhi. Tente novemente")
                return False
            elif guess > number:
                print(f"O número {guess} é maior do que o número que eu escolhi. Tente novemente")
                return False
        else:
            print("Valores não permitidos. Tente novamente")
    elif language == "EN":
        print("")
        guess = input(f"Choose a number between 0 and {max_number}: ")
        guess = int(guess)
        
        if guess >= 0 and guess <= max_number:
            if int(guess) == number:
                print("")
                print("+===============================+")
                print("|       CONGRATULATIONS!        |")
                print("|    You've found the number!   |")
                print("+===============================+")
                return True
            elif guess < number:
                print(f"The number {guess} is smaller than the number that I chose. Try again")
                return False
            elif guess > number:
                print(f"The number {guess} is bigger than the number that I chose. Try again")
                return False
        else:
            print("Wrong value. Try again")
    else:
        # Any other language implemented yet. Future.
        pass