import prompt
from colorama import Fore, Style
from colorama import init


def run(game):
    init(autoreset=True)
    print(Fore.CYAN + Style.BRIGHT + 'Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print()
    round = 3
    while round != 0:
        (question, correct_answer) = game.get_conditions()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(
                Fore.RED +
                "'{}' is wrong answer ;(. Correct answer was '{}'."
                "\nLet\'s try again, {}!"
                .format(answer, correct_answer, name))
            break
        print(Fore.GREEN + 'Correct!')
        round -= 1
    else:
        print(Fore.BLUE + Style.BRIGHT + 'Congratulations, {}!'.format(name))
