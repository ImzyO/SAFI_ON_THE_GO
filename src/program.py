from colorama import Fore
#import program_guests
import program_host
import models.mongo_setup as mongo_setup


def main():
    mongo_setup.global_init()

    print_header()

    try:
        while True:
            if find_user_intent() == 'book':
                program_guests.run()
            else:
                program_hosts.run()
    except KeyboardInterrupt:
        return


def print_header():
    smiley_face = \
        """..........                                   
                                   ..&@...@,...                                 
                                  ....%...@....                                 
                                  ../.......@.(                                 
                                    (.......("""

    print(Fore.WHITE + '****************  SNAKE BnB  ****************')
    print(Fore.YELLOW + smiley_face)
    print(Fore.WHITE + '*********************************************')
    print()
    print("Welcome to SAFI ON THE GO!")
    print("Why are you here?")
    print()


def find_user_intent():
    print("[g] Book a car wash appointment")
    print("[h] Offer car wash services")
    print()
    choice = input("Are you a [g]uest or [h]ost? ")
    if choice == 'h':
        return 'offer'

    return 'book'


if __name__ == '__main__':
    main()
