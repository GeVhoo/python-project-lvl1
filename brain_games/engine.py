import prompt
from colorama import Fore, Style
from colorama import init
init(autoreset=True)


def engine(game):
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
        if answer == correct_answer:
            print(Fore.GREEN + 'Correct!')
            round -= 1
        else:
            return print(
                Fore.RED +
                "'{}' is wrong answer ;(. Correct answer was '{}'."
                "\nLet\'s try again, {}!"
                .format(answer, correct_answer, name))
    print(Fore.BLUE + Style.BRIGHT + 'Congratulations, {}!'.format(name))
