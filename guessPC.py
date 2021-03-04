import random
import funcs

max_number = 1000
correct_answer = False

funcs.presentation()
language = funcs.language()

if language == "PT-BR":
    print(f"Eu irei escolher um número entre 0 e {max_number} e você deverá achar qual é esse número. Está preparado?")
    answer = input("Pronto para continuar? [Sim/Não] ")
elif language == "EN":
    print(f"I'll choose a number between 0 and {max_number} and you should find wich number it is. Are you ready?")
    answer = input("Let's go? [Yes/No] ")
else:
    # Any other language implemented yet. Future.
    pass

while (answer.lower() != "sim" or answer.lower() != "não"
       or answer.lower() != "s" or answer.lower() != "n"
       or answer.lower() != "yes" or answer.lower() != "no"
       or answer.lower() != "y"):
    if (answer.lower() == "sim" or answer.lower() == "s"
        or answer.lower() == "yes" or answer.lower() == "y"):
        number = random.randint(0,max_number)
        if language == "PT-BR":
            print("Pronto! Já escolhi o número. Agora é com você!")
        elif language == "EN":
            print("OK! I've already chosen the number. Now it's up to you!")
        else:
            # Any other language implemented yet. Future.
            pass
            
        while correct_answer != True:
            correct_answer = funcs.tentativa(number, max_number, language)
            if correct_answer == True:
                break
        break
    elif answer.lower() == "não" or answer.lower() == "no" or answer.lower() == "n":
        print("")
        print("+========+")
        print("|  Bye!  |")
        print("| Tchau! |")
        print("+========+")
        print("")
        break
    else:
        print("Oops! It seems that you didn't choose a correct answer. Say just Yes or No")
        print("Opa! Parece que você não digitou a resposta corretamente. Digite somente Sim ou Não")
        answer = input("Ready? [Yes or No] | Pronto para continuar? [Digite Sim ou Não] ")