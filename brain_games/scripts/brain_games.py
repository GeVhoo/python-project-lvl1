#!/usr/bin/env python3

from brain_games.scripts.games.brain_calc import brain_calc
from brain_games.scripts.games.brain_even import brain_even
from brain_games.scripts.games.brain_gcd import brain_gcd
from brain_games.scripts.games.brain_prime import brain_prime
from brain_games.scripts.games.brain_progression import brain_progression
from random import choice
import prompt
from colorama import Fore, Style
from colorama import init
init(autoreset=True)


def main():
    print(Fore.CYAN + Style.BRIGHT + 'Welcome to the Brain Games!')
    print()
    print(Fore.CYAN + 'Choose a game from the list:')
    print('1. Parity Check.')
    print('2. Calculator.')
    print('3. Greatest Common Divisor.')
    print('4. Arithmetic Progression.')
    print('5. Is The Number Prime?')
    print('6. Choose randomly.')
    print()
    game = prompt.string('Enter the game number to start: ')
    print()
    all_game = (brain_calc, brain_even, brain_gcd, brain_prime, brain_progression) # noqa
    random_game = choice(all_game)
    if game == '1':
        brain_even()
    elif game == '2':
        brain_calc()
    elif game == '3':
        brain_gcd()
    elif game == '4':
        brain_progression()
    elif game == '5':
        brain_prime()
    elif game == '6':
        random_game()
    else:
        print(Fore.BLUE + Style.BRIGHT + 'Good bye!')


if __name__ == '__main__':
    main()
